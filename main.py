import sys
from quetzal import *
from gui import (Ui_MainWindow, QtWidgets, QtGui, QtCore)
from about_dialog import Ui_About_Dialog
from cal_dialog import Ui_Cal_Dialog
from clone_dialog import Ui_Clone_Dialog
from confirm_dialog import Ui_Confirm_Dialog
from pyqtspinner.spinner import WaitingSpinner
from settings_dialog import Ui_Settings_Dialog
from tree_dialog import Ui_Tree_Dialog
from threading import Timer
from workers import (Worker, WorkerSignals, Updater)


def statusDisplay(_elem_, _status_=True):
    if _status_:
        _elem_.setText('Success!')
        _elem_.show()
    else:
        _elem_.setText('Oops! Process aborted')
        _elem_.show()
    Timer(3, _elem_.hide).start()


class QuetzalApp(Ui_MainWindow):
    """tie functionality to qt frontend"""

    def treeDialog(self, params):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Tree_Dialog(params)
        dialog.ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted and dialog.ui.current_value != '':
            return dialog.ui.current_value
        return False

    def calendarDialog(self, params):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Cal_Dialog(params)
        dialog.ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            return dialog.ui.date_val
        return False

    def fileDialog(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle('Choose Directory')
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOptions(QtWidgets.QFileDialog.ShowDirsOnly)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            return dialog.selectedFiles()[0]
        return False

    def cloneDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Clone_Dialog()
        dialog.ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted and dialog.ui.clone_params:
            return dialog.ui.clone_params
        return False

    def confDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Settings_Dialog(withConfig())
        dialog.ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted and dialog.ui.new_conf != '':
            return dialog.ui.new_conf
        return False

    def confirmDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Confirm_Dialog(self.full_selected['slug'])
        dialog.ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            return True
        return False

    def aboutDisplay(self):
        """about dilog window"""
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_About_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def currentSelection(self):
        """dynamically handles current selection based on bar and list"""
        if self.last_focused == 'tree' and self.projects_tree.currentItem():
            _val_ = self.projects_tree.currentItem().text(0)
            self.search_bar.setText(_val_)
        elif self.last_focused == 'line' and self.search_bar.text():
            _val_ = self.search_bar.text()
        else:
            return False

        if _val_ and getByContext(_val_):
            self.current_selected = getByContext(_val_)
            self.full_selected = [qz for qz in getProjects(
            ) if qz['abs_dir'] == self.current_selected][0]
        else:
            self.error_display.setText('No project with that name or path')

    def changeSettings(self):
        new_config = self.confDialog()
        withConfig(new_config)

    def qzOpen(self):
        """open local editor middleman"""
        openByContext(self.current_selected, self.debug_checkbox.isChecked())

    def qzTerminal(self):
        """open terminal middleman"""
        if withConfig('terminal'):
            openInTerminal(self.current_selected)
        else:
            self.error_display.setText('Please set your terminal config first')

    def qzExplorer(self):
        """open file explorer middleman"""
        if openInExplorer(self.current_selected) == 'done':
            statusDisplay(self.error_display)
        else:
            statusDisplay(self.error_display, False)

    def qzUpdate(self):
        """updater middleman"""
        if isinstance(self.current_selected, str) and len(self.current_selected) > 0:
            slug = self.full_selected['slug']

            def updating(progress_callback):
                updateProject(self.current_selected)
                progress_callback.emit(print('updating'))

            def printSuccess():
                self.spinner.stop()
                self.error_display.setText(f'{slug} successfully updated!')
                self.error_display.show()
                Timer(3, self.error_display.hide).start()

            def printReject():
                self.spinner.stop()
                self.error_display.setText(f'Sorry! {slug} was NOT updated...')
                Timer(3, self.error_display.hide).start()

            def showUpdating(msg):
                print(msg)

            up_stat = Worker(updating)
            up_stat.signals.result.connect(showUpdating)
            up_stat.signals.finished.connect(printSuccess)
            up_stat.signals.progress.connect(showUpdating)
            up_stat.signals.error.connect(printReject)

            self.threadpool.start(up_stat)
            self.spinner.start()

            if up_stat == 'done':
                statusDisplay(self.error_display)
            else:
                statusDisplay(self.error_display, False)

    def qzUpdateAll(self):
        """update all middleman"""
        if self.is_updating:
            return False

        self.is_updating = True

        def update_status(prop=False):
            do_update = Updater(
                self.debug_checkbox.isChecked(), self.over_ride.isChecked())

            props = {
                'prev_slug': '',
                'curr_slug': '',
                'ok_updated': [],
                'curr_status': ''
            }

            up_stat.signals.result.connect(showUpdatingAll)
            up_stat.signals.progress.connect(showUpdatingAll)

            def showUpdatingAll():
                print(do_update.status)
                props['prev_slug'] = props['curr_slug']
                props['curr_slug'] = do_update._current
                props['ok_updated'].append(props['prev_slug'])
                props['curr_status'] = do_update.status
                self.error_display.setText(
                    f'{props["prev_slug"]} successfully updated!')

            if not prop:
                self.spinner.start()
                return do_update
            try:
                return props[prop]
            except KeyError:
                raise f"{prop} is not a valid key"

        def printSuccessAll():
            self.spinner.stop()
            self.error_display.setText('Projects successfully updated!')
            self.error_display.show()
            Timer(3, self.error_display.hide).start()
            self.is_updating = False

        def printRejectAll():
            self.spinner.stop()
            last_success = update_status('ok_updated')[:-1]
            failure_at = update_status('curr_slug')
            self.error_display.setText(
                f'Sorry! {last_success} was updated, but not {failure_at}...')
            Timer(3, self.error_display.hide).start()
            self.is_updating = False

        up_stat = Worker(update_status)
        up_stat.signals.finished.connect(printSuccessAll)
        up_stat.signals.error.connect(printRejectAll)

        self.threadpool.start(update_status)

    def qzRefreshAll(self):
        """init refresh output handler"""
        if doInit(True) == 'done':
            statusDisplay(self.error_display)
            self.qzRefresh()
        else:
            statusDisplay(self.error_display, False)

    def setCloneParams(self):
        """interim multiple prompt setup"""
        params = self.cloneDialog()

        if params:
            _dir_ = f"{mainDir()}/{params['name']}"
            _url_ = params['url']
            do_debug = params['debug']

            if create(_dir_, _url_, do_debug) == 'done':
                statusDisplay(self.error_display)
            else:
                statusDisplay(self.error_display, False)
        else:
            statusDisplay(self.error_display, False)

    def appendDirParams(self):
        """add watched directory middleman"""
        abs_path = self.fileDialog()
        if abs_path and abs_path != None:
            if appendDir(abs_path) == 'done':
                statusDisplay(self.error_display)
                self.qzRefresh()
            else:
                statusDisplay(self.error_display, False)

    def rmDirParams(self):
        """remove watched directory middleman"""
        tree_data = getDirs().items()

        abs_path = self.treeDialog({
            'accept': 'Remove From List',
            'data': tree_data,
        })

        if appendDir(abs_path) == 'done':
            statusDisplay(self.error_display)
            self.qzRefreshAll()
            self.qzRefresh()
        else:
            statusDisplay(self.error_display, False)

    def changeMainDir(self):
        """change main scanned projects directory"""
        all_opts = getDirs().items()
        new_main_dir = self.treeDialog({'data': all_opts})

        main_dir_set = mainDir(new_main_dir)
        if main_dir_set == 'done':
            statusDisplay(self.error_display)
        else:
            statusDisplay(self.error_display, False)

    def appendQzParams(self):
        """add project middleman"""
        new_dir = self.fileDialog()

        if new_dir:
            if appendProject(new_dir) == 'done':
                statusDisplay(self.error_display)
                self.qzRefresh()
                self.qzRefreshAll()
            else:
                statusDisplay(self.error_display, False)

    def rmQzParams(self):
        """remove project middleman"""
        to_rm = self.treeDialog({
            'data': [(qz['slug'], qz['abs_dir']) for qz in getProjects()],
        })

        if to_rm:
            if deleteProject(to_rm) == 'done':
                statusDisplay(self.error_display)
                self.qzRefresh()
                self.qzRefreshAll()
            else:
                statusDisplay(self.error_display, False)

    def qzRefresh(self):
        """refresh project tree"""
        self.projects_tree.clear()
        for _qz_ in getProjects(True):
            if _qz_['favorited'] == 'true':
                _fav_ = u'\u2713'
            else:
                _fav_ = ''

            if _qz_['due_date'] == 'none' or _qz_['due_date'] == '':
                _date_ = ''
            else:
                date_list = _qz_['due_date'].split(', ')
                D = [int(d) for d in date_list[0].split(' ')]
                T = [int(t) for t in date_list[1].split(':')]
                _d_ = QtCore.QDate(
                    D[2], D[1], D[0]).toString('ddd MMM dd yyyy')
                _t_ = QtCore.QTime(T[0], T[1]).toString('h:mm ap')
                _date_ = f"{_d_}, {_t_}"

            qz_item = QtWidgets.QTreeWidgetItem(self.projects_tree, [
                _qz_['slug'],
                _qz_['abs_dir'].replace(f"{Path.home()}/", ''),
                _fav_,
                _date_
            ])

            qz_item.setFlags(qz_item.flags() | 128 | 1)
            qz_item.setTextAlignment(2, QtCore.Qt.AlignCenter)

        statusDisplay(self.error_display)

    def qzDeadline(self):
        """change project deadlines"""
        cal_data = {
            'name': self.full_selected['slug'],
            'set_date': '',
            'set_time': ''
        }

        if self.full_selected['due_date'] != 'none':
            if len(self.full_selected['due_date'].split(',')) > 0:
                cal_data['set_date'] = self.full_selected['due_date'].split(',')[
                    0]
                cal_data['set_time'] = self.full_selected['due_date'].split(',')[
                    1]

        new_deadline = self.calendarDialog(cal_data)
        if new_deadline:
            if setDeadline(self.full_selected['slug'], new_deadline) == 'done':
                statusDisplay(self.error_display)
                self.qzRefresh()
            else:
                statusDisplay(self.error_display, False)

    def qzFavToggle(self):
        if toggleFavorite(self.current_selected) == 'done':
            statusDisplay(self.error_display)
            self.qzRefresh()
        else:
            statusDisplay(self.error_display, False)

    def contextMenu(self, position):
        """context menu items"""
        menu = QtWidgets.QMenu()
        menu.setStyleSheet("""
            QMenu {
                background-color: #434348;
                color: #f5f6f7;
            }
            
            QMenu::item:selected {
                background-color: #00B554;
            }
            
            QMenu::item:pressed {
                background-color: #00B554;
            }
            """)
        fav_action = menu.addAction('Toggle Favorited')
        deadline_action = menu.addAction('Change Deadline')
        rm_action = menu.addAction('Remove From List')
        action = menu.exec_(self.projects_tree.mapToGlobal(position))
        if action == fav_action:
            self.qzFavToggle()
        elif action == deadline_action:
            self.qzDeadline()
        elif action == rm_action:
            if self.confirmDialog():
                if deleteProject(self.current_selected) == 'done':
                    statusDisplay(self.error_display)
                    self.qzRefresh()
                else:
                    statusDisplay(self.error_display, False)

    def lineEditFocus(self):
        self.last_focused = 'line'
        self.currentSelection()

    def treeFocus(self):
        self.last_focused = 'tree'
        self.currentSelection()

    def __init__(self, window):
        self.setupUi(window)
        self.threadpool = QtCore.QThreadPool()
        self.current_selected = ''
        self.full_selected = ''
        self.spinner = WaitingSpinner(
            self.centralwidget,
            roundness=70.0, opacity=15.0,
            fade=70.0, radius=10.0, lines=12,
            line_length=10.0, line_width=5.0,
            speed=1.0, color=(67, 67, 72)
        )
        self.is_updating = False

        if not isInit():
            doInit(False)

        qz_tree = self.projects_tree
        qz_data = getProjects(True)

        """set dynamic gui object values"""
        self.search_bar.setPlaceholderText('Filter')
        self.error_display.setText('')

        for _qz_ in qz_data:
            if _qz_['favorited'] == 'true':
                _fav_ = u'\u2713'
            else:
                _fav_ = ''

            if _qz_['due_date'] == 'none' or _qz_['due_date'] == '':
                _date_ = ''
            else:
                date_list = _qz_['due_date'].split(', ')
                D = [int(d) for d in date_list[0].split(' ')]
                T = [int(t) for t in date_list[1].split(':')]
                _d_ = QtCore.QDate(
                    D[2], D[1], D[0]).toString('ddd MMM dd yyyy')
                _t_ = QtCore.QTime(T[0], T[1]).toString('h:mm ap')
                _date_ = f"{_d_}, {_t_}"

            qz_item = QtWidgets.QTreeWidgetItem(qz_tree, [
                _qz_['slug'],
                _qz_['abs_dir'].replace(f"{Path.home()}/", ''),
                _fav_,
                _date_
            ])

            qz_item.setFlags(qz_item.flags() | 128 | 1)
            qz_item.setTextAlignment(2, QtCore.Qt.AlignCenter)

        """connect gui objects to respective functions"""
        qz_tree.customContextMenuRequested.connect(self.contextMenu)
        qz_tree.setEditTriggers(qz_tree.NoEditTriggers)
        qz_tree.doubleClicked.connect(self.qzOpen)
        qz_tree.currentItemChanged.connect(self.treeFocus)
        self.search_bar.textChanged.connect(self.lineEditFocus)
        self.open_button.clicked.connect(self.qzOpen)
        self.pull_button.clicked.connect(self.qzUpdate)
        self.pull_all.clicked.connect(self.qzUpdateAll)
        self.open_terminal.clicked.connect(self.qzTerminal)
        self.open_explorer.clicked.connect(self.qzExplorer)

        """file dialog creation for menu options"""
        self.actionReset.triggered.connect(self.qzRefreshAll)
        self.actionChange_Main_Folder.triggered.connect(self.changeMainDir)
        self.actionCreate_New.triggered.connect(self.setCloneParams)
        self.actionAdd_Project_Path.triggered.connect(self.appendQzParams)
        self.actionDelete_Project_Path.triggered.connect(self.rmQzParams)
        self.actionAdd_Watched_Folder.triggered.connect(self.appendDirParams)
        self.actionRemove_Watched_Folder.triggered.connect(self.rmDirParams)
        self.actionChange_Settings.triggered.connect(self.changeSettings)
        self.actionAbout.triggered.connect(self.aboutDisplay)
        self.actionRefresh.triggered.connect(self.qzRefresh)
        self.actionQuit.triggered.connect(sys.exit)
        self.actionLogin.triggered.connect(loginHandler)
        self.actionLogout.triggered.connect(logoutHandler)


app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("images/quetzal.png"))
MainWindow = QtWidgets.QMainWindow()

ui = QuetzalApp(MainWindow)

MainWindow.show()
app.exec_()
