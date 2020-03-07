import sys
from quetzal import *
from gui import (Ui_MainWindow, QtWidgets, QtGui, QtCore)
from dialogs.about_dialog import Ui_About_Dialog
from dialogs.cal_dialog import Ui_Cal_Dialog
from dialogs.clone_dialog import Ui_Clone_Dialog
from dialogs.confirm_dialog import Ui_Confirm_Dialog
from dialogs.settings_dialog import Ui_Settings_Dialog
from dialogs.tree_dialog import Ui_Tree_Dialog
from pyqtspinner.spinner import WaitingSpinner
from get_styles import STYLES
from threading import Timer
from workers import (FileWatcher, Updater)


class QuetzalApp(Ui_MainWindow):
    """tie functionality to qt frontend"""

    def __init__(self, window):
        self.setupUi(window)

        if not isInit():
            doInit()

        self.threadpool = QtCore.QThreadPool()
        self.filewatcher = FileWatcher()
        self.filewatcher.signals.filechange.connect(self.qzRefresh)
        self.filewatcher.signals.dirchange.connect(self.qzRefreshAll)
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

        """set dynamic gui object values"""
        self.search_bar.setPlaceholderText('Search by name or path')
        self.error_display.setText('Welcome!')
        Timer(3, self.clearMessage).start()
        self.qzRefresh(True)

        """connect gui objects to respective functions"""
        self.projects_tree.customContextMenuRequested.connect(self.contextMenu)
        self.projects_tree.setEditTriggers(self.projects_tree.NoEditTriggers)
        self.projects_tree.doubleClicked.connect(self.qzOpen)
        self.projects_tree.currentItemChanged.connect(self.treeFocus)
        self.projects_tree.adjustSize()
        self.projects_tree.resizeColumnToContents(0)
        self.projects_tree.resizeColumnToContents(1)
        self.projects_tree.resizeColumnToContents(3)
        self.search_bar.textChanged.connect(self.lineEditFocus)
        self.open_button.clicked.connect(self.qzOpen)
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
        message = f"Are you sure you want to delete {self.full_selected['slug']}?"
        dialog.ui = Ui_Confirm_Dialog(message)
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
            self.statusDisplay()
        else:
            self.statusDisplay(False)

    def qzUpdate(self):
        """updater middleman"""
        if self.is_updating:
            return False

        if isinstance(self.current_selected, str) and len(self.current_selected) > 0:
            slug = self.full_selected['slug']

            def printEnd(message):
                self.is_updating = False
                self.spinner.stop()
                if message == 'success':
                    self.error_display.setText(f'{slug} successfully updated!')
                else:
                    self.error_display.setText(f'Error: {message}')
                Timer(3, self.clearMessage).start()

            def printReject(error):
                # self.is_updating = False
                # self.spinner.stop()
                self.error_display.setText(f'Error: {error}')
                # Timer(3, self.clearMessage).start()

            def showUpdating(current_updating):
                self.is_updating = True
                self.spinner.start()
                self.error_display.setText(f'Now updating {current_updating}')

            def percentCompleted(_ix_, _len_):
                print(_ix_/_len_)

            up_stat = Updater(self.current_selected, self.debug_checkbox.isChecked(
            ), self.over_ride.isChecked())
            up_stat.signals.current.connect(showUpdating)
            up_stat.signals.finished.connect(printEnd)
            up_stat.signals.progress.connect(percentCompleted)
            up_stat.signals.error.connect(printReject)

            self.threadpool.start(up_stat)
            self.spinner.start()

            if up_stat == 'done':
                self.statusDisplay()
            else:
                self.statusDisplay(False)

    def qzUpdateAll(self):
        """update all middleman"""
        if self.is_updating:
            return False

        current = ''

        def printEnd():
            self.is_updating = False
            self.spinner.stop()
            self.error_display.setText(f'{current} successfully updated!')
            Timer(3, self.clearMessage).start()

        def printReject(error):
            self.is_updating = False
            self.spinner.stop()
            self.error_display.setText(f'Error: {error}')
            Timer(3, self.clearMessage).start()

        def showUpdating(current_updating):
            current = current_updating
            self.error_display.setText(f'Now updating {current_updating}')

        def percentCompleted(percentage):
            print(percentage)

        def reAssignButton():
            self.pull_all.setText('Abort')
            self.pull_all.clicked.connect(processAbort)

        def processAbort():
            Updater('stop')
            self.spinner.stop()
            self.pull_all.setText('Update All')
            self.pull_all.clicked.connect(self.qzUpdateAll)
            self.is_updating = False

        up_stat = Updater('all', self.debug_checkbox.isChecked(),
                          self.over_ride.isChecked())
        up_stat.signals.current.connect(showUpdating)
        up_stat.signals.finished.connect(printEnd)
        up_stat.signals.error.connect(printReject)
        up_stat.signals.progress.connect(percentCompleted)

        self.is_updating = True
        self.spinner.start()
        self.threadpool.start(update_status)
        Timer(3, reAssignButton).start()

    def qzRefreshAll(self):
        """init refresh output handler"""
        if doInit(True) == 'done':
            self.statusDisplay()
            self.qzRefresh()
        else:
            self.statusDisplay(False)

    def setCloneParams(self):
        """interim multiple prompt setup"""
        params = self.cloneDialog()

        if params:
            _dir_ = f"{mainDir()}/{params['name']}"
            _url_ = params['url']
            do_debug = params['debug']

            if create(_dir_, _url_, do_debug) == 'done':
                self.statusDisplay()
            else:
                self.statusDisplay(False)
        else:
            self.statusDisplay(False)

    def appendDirParams(self):
        """add watched directory middleman"""
        abs_path = self.fileDialog()
        if not abs_path:
            return self.statusDisplay(False)
        print(abs_path)

        def appendSuccess():
            self.statusDisplay()
            self.qzRefresh()

        def appendFail(error):
            print(error)
            self.statusDisplay(False)

        adding_dir = self.filewatcher.addWatched(str(abs_path))
        adding_dir.signals.success.connect(appendSuccess)
        adding_dir.signals.failure.connect(appendFail)

        self.threadpool.start(adding_dir)

    def rmDirParams(self):
        """remove watched directory middleman"""
        tree_data = getDirs().items()

        abs_path = self.treeDialog({
            'accept': 'Remove From List',
            'data': tree_data,
        })

        def rmSuccess():
            self.statusDisplay()
            self.qzRefreshAll()
            self.qzRefresh()

        def rmFail():
            self.statusDisplay(False)

        if not abs_path:
            return rmFail()

        removing_dir = self.filewatcher.rmWatched(abs_path)
        removing_dir.signals.success.connect(rmSuccess)
        removing_dir.signals.failure.connect(rmFail)

        self.threadpool.start(removing_dir)

    def changeMainDir(self):
        """change main scanned projects directory"""
        all_opts = getDirs().items()
        new_main_dir = self.treeDialog({'data': all_opts})

        main_dir_set = mainDir(new_main_dir)
        if main_dir_set == 'done':
            self.statusDisplay()
        else:
            self.statusDisplay(False)

    def appendQzParams(self):
        """add project middleman"""
        new_dir = self.fileDialog()

        if new_dir:
            if appendProject(new_dir) == 'done':
                self.statusDisplay()
                self.qzRefresh()
                self.qzRefreshAll()
            else:
                self.statusDisplay(False)

    def rmQzParams(self):
        """remove project middleman"""
        to_rm = self.treeDialog({
            'data': [(qz['slug'], qz['abs_dir']) for qz in getProjects()],
        })

        if to_rm:
            if deleteProject(to_rm) == 'done':
                self.statusDisplay()
                self.qzRefresh()
                self.qzRefreshAll()
            else:
                self.statusDisplay(False)

    def qzRefresh(self, initiating=False):
        """refresh project tree"""
        self.projects_tree.clear()
        for _qz_ in getProjects():
            if _qz_['favorited'] == 'true':
                _fav_ = u'\u2714'
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

        if not initiating:
            self.statusDisplay()

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
                self.statusDisplay()
                self.qzRefresh()
            else:
                self.statusDisplay(False)

    def qzFavToggle(self):
        if toggleFavorite(self.current_selected) == 'done':
            self.statusDisplay()
            self.qzRefresh()
        else:
            self.statusDisplay(False)

    def contextMenu(self, position):
        """context menu items"""
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(STYLES())
        fav_action = menu.addAction('Toggle Favorited')
        deadline_action = menu.addAction('Change Deadline')
        update_action = menu.addAction('Update Project')
        rm_action = menu.addAction('Remove From List')
        action = menu.exec_(self.projects_tree.mapToGlobal(position))
        if action == fav_action:
            self.qzFavToggle()
        elif action == deadline_action:
            self.qzDeadline()
        elif action == rm_action:
            if self.confirmDialog():
                if deleteProject(self.current_selected) == 'done':
                    self.statusDisplay()
                    self.qzRefresh()
                else:
                    self.statusDisplay(False)
        elif action == update_action:
            self.qzUpdate()

    def lineEditFocus(self):
        self.last_focused = 'line'
        self.currentSelection()

    def treeFocus(self):
        self.last_focused = 'tree'
        self.currentSelection()

    def clearMessage(self):
        self.error_display.setText('')

    def statusDisplay(self, _status_=True):
        if _status_:
            self.error_display.setText('Success!')
        else:
            self.error_display.setText('Oops! Process aborted')
        Timer(3, self.clearMessage).start()


app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("images/quetzal.png"))
MainWindow = QtWidgets.QMainWindow()

ui = QuetzalApp(MainWindow)

MainWindow.show()
app.exec_()
