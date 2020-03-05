# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiQT.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 604)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("""
    QWidget{ font: 75 11pt \\\"Noto Sans\\\"; }

    QWidget#centralwidget {
        background-color: #f5f6f7;
    }

    QMainWindow {
        background-color: #f5f6f7; 
        color: #434348;
    }

    QPushButton {
        border-width:2px;
        background-color: #f5f6f7;
        color: #434348;
        border-color: transparent;
        border-radius: 3px;
        border-style: outset;
        font-weight: 500;
        padding: 7px;
    }

    QPushButton:hover {
        background-color: #00B554;
        color: #f5f6f7;
    }

    QPushButton:pressed {
        border-color: #f5f6f7;
    }

    QCheckBox {
        font-weight: 500;
    } 

    QCheckBox::indicator {
        background-color: rgba(65, 65, 65, 0.2);
        border-radius: 3px;
        border-width: 1px;
        border-color: transparent;
        border-style: inset;
        padding: 8px;
    }

    QCheckBox::indicator:hover {
        border-color: #00B554;
        background-color: rgba(65, 65, 65, 0.3);
    }

    QCheckBox::indicator:checked {
        border-color: transparent;
        background-color: #00B554;
    }

    QLabel {
        font-weight: 500;
        color: #00B554;
    }

    QTreeWidget {
        font-weight: 400;
        background-color: #f5f6f7;
        border-width: 2px;
        border-color: #9F9EA5;
        border-radius: 3px;
        border-style: ridge;
    }
    
    QTreeWidget QHeaderView::section {
        background-color: #434348;
        color: #f5f6f7;
    }

    QTreeWidget::item:hover {
        background-color: #00B554;
        color: #f5f6f7;
    }

    QTreeWidget::item:selected {
        background-color: #00B554;
        color: #f5f6f7;
    }

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

    QMenuBar {
        background-color: rgba(65, 65, 65, 0.1);
        color: #692EF0;
    }

    QMenuBar::item {
        background-color: transparent;
        color: #9F9EA5;
    }

    QMenuBar::item:selected {
        color: #434348;
    }

    QLineEdit {
        color: #9F9EA5;
    }

    QLineEdit:hover {
        color: #434348;
    }

    QLineEdit:focus {
        color: #00B554;
    }
""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 731, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_bar = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy)
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_2.addWidget(self.search_bar)
        self.over_ride = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.over_ride.sizePolicy().hasHeightForWidth())
        self.over_ride.setSizePolicy(sizePolicy)
        self.over_ride.setObjectName("over_ride")
        self.horizontalLayout_2.addWidget(self.over_ride)
        self.pull_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pull_button.sizePolicy().hasHeightForWidth())
        self.pull_button.setSizePolicy(sizePolicy)
        self.pull_button.setFlat(False)
        self.pull_button.setObjectName("pull_button")
        self.horizontalLayout_2.addWidget(self.pull_button)
        self.pull_all = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pull_all.sizePolicy().hasHeightForWidth())
        self.pull_all.setSizePolicy(sizePolicy)
        self.pull_all.setObjectName("pull_all")
        self.horizontalLayout_2.addWidget(self.pull_all)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.projects_tree = QtWidgets.QTreeWidget(self.layoutWidget)
        self.projects_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.projects_tree.setObjectName("projects_tree")
        self.gridLayout.addWidget(self.projects_tree, 1, 0, 1, 2)
        self.error_display = QtWidgets.QLabel(self.layoutWidget)
        self.error_display.setObjectName("error_display")
        self.gridLayout.addWidget(self.error_display, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.debug_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.debug_checkbox.sizePolicy().hasHeightForWidth())
        self.debug_checkbox.setSizePolicy(sizePolicy)
        self.debug_checkbox.setObjectName("debug_checkbox")
        self.horizontalLayout.addWidget(self.debug_checkbox)
        self.open_terminal = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.open_terminal.sizePolicy().hasHeightForWidth())
        self.open_terminal.setSizePolicy(sizePolicy)
        self.open_terminal.setObjectName("open_terminal")
        self.horizontalLayout.addWidget(self.open_terminal)
        self.open_explorer = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.open_explorer.sizePolicy().hasHeightForWidth())
        self.open_explorer.setSizePolicy(sizePolicy)
        self.open_explorer.setObjectName("open_explorer")
        self.horizontalLayout.addWidget(self.open_explorer)
        self.open_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuProjects = QtWidgets.QMenu(self.menubar)
        self.menuProjects.setObjectName("menuProjects")
        self.menuLocations = QtWidgets.QMenu(self.menubar)
        self.menuLocations.setObjectName("menuLocations")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuQuetzal = QtWidgets.QMenu(self.menubar)
        self.menuQuetzal.setObjectName("menuQuetzal")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_New = QtWidgets.QAction(MainWindow)
        self.actionCreate_New.setObjectName("actionCreate_New")
        self.actionAdd_Project_Path = QtWidgets.QAction(MainWindow)
        self.actionAdd_Project_Path.setObjectName("actionAdd_Project_Path")
        self.actionDelete_Project_Path = QtWidgets.QAction(MainWindow)
        self.actionDelete_Project_Path.setObjectName(
            "actionDelete_Project_Path")
        self.actionAdd_Watched_Folder = QtWidgets.QAction(MainWindow)
        self.actionAdd_Watched_Folder.setObjectName("actionAdd_Watched_Folder")
        self.actionRemove_Watched_Folder = QtWidgets.QAction(MainWindow)
        self.actionRemove_Watched_Folder.setObjectName(
            "actionRemove_Watched_Folder")
        self.actionChange_Main_Folder = QtWidgets.QAction(MainWindow)
        self.actionChange_Main_Folder.setObjectName("actionChange_Main_Folder")
        self.actionChange_Settings = QtWidgets.QAction(MainWindow)
        self.actionChange_Settings.setObjectName("actionChange_Settings")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuProjects.addAction(self.actionRefresh)
        self.menuProjects.addAction(self.actionCreate_New)
        self.menuProjects.addSeparator()
        self.menuProjects.addAction(self.actionAdd_Project_Path)
        self.menuProjects.addAction(self.actionDelete_Project_Path)
        self.menuLocations.addAction(self.actionChange_Main_Folder)
        self.menuLocations.addSeparator()
        self.menuLocations.addAction(self.actionAdd_Watched_Folder)
        self.menuLocations.addAction(self.actionRemove_Watched_Folder)
        self.menuSettings.addAction(self.actionChange_Settings)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionReset)
        self.menuQuetzal.addAction(self.actionLogin)
        self.menuQuetzal.addAction(self.actionLogout)
        self.menuQuetzal.addSeparator()
        self.menuQuetzal.addAction(self.actionAbout)
        self.menuQuetzal.addAction(self.actionQuit)
        self.menubar.addAction(self.menuQuetzal.menuAction())
        self.menubar.addAction(self.menuProjects.menuAction())
        self.menubar.addAction(self.menuLocations.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.search_bar, self.over_ride)
        MainWindow.setTabOrder(self.over_ride, self.pull_button)
        MainWindow.setTabOrder(self.pull_button, self.pull_all)
        MainWindow.setTabOrder(self.pull_all, self.projects_tree)
        MainWindow.setTabOrder(self.projects_tree, self.debug_checkbox)
        MainWindow.setTabOrder(self.debug_checkbox, self.open_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quetzal"))
        self.over_ride.setText(_translate("MainWindow", "Override"))
        self.pull_button.setText(_translate("MainWindow", "Update Selected"))
        self.pull_all.setText(_translate("MainWindow", "Update All"))
        self.projects_tree.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.projects_tree.headerItem().setText(1, _translate("MainWindow", "Location"))
        self.projects_tree.headerItem().setText(
            2, _translate("MainWindow", "Favorited"))
        self.projects_tree.headerItem().setText(3, _translate("MainWindow", "Due Date"))
        self.error_display.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" color:#212121;\">TextLabel</span></p></body></html>"))
        self.debug_checkbox.setText(_translate("MainWindow", "Debug"))
        self.open_terminal.setText(_translate("MainWindow", ">_"))
        self.open_explorer.setText(_translate("MainWindow", u"\U0001F4C2"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.menuProjects.setTitle(_translate("MainWindow", "Projects"))
        self.menuLocations.setTitle(_translate("MainWindow", "Locations"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuQuetzal.setTitle(_translate("MainWindow", "Quetzal"))
        self.actionCreate_New.setText(_translate("MainWindow", "Create New"))
        self.actionAdd_Project_Path.setText(
            _translate("MainWindow", "Add Project Path"))
        self.actionDelete_Project_Path.setText(
            _translate("MainWindow", "Delete Project Path"))
        self.actionAdd_Watched_Folder.setText(
            _translate("MainWindow", "Add Watched Folder"))
        self.actionRemove_Watched_Folder.setText(
            _translate("MainWindow", "Remove Watched Folder"))
        self.actionChange_Main_Folder.setText(
            _translate("MainWindow", "Change Main Folder"))
        self.actionChange_Settings.setText(
            _translate("MainWindow", "Settings"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
