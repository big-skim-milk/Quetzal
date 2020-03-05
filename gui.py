# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiQT.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from get_styles import STYLES
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 608)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(STYLES())
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
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy)
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_2.addWidget(self.search_bar)
        self.error_display = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.error_display.sizePolicy().hasHeightForWidth())
        self.error_display.setSizePolicy(sizePolicy)
        self.error_display.setStyleSheet("color: rgb(204, 0, 0);")
        self.error_display.setObjectName("error_display")
        self.horizontalLayout_2.addWidget(self.error_display)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.projects_tree = QtWidgets.QTreeWidget(self.layoutWidget)
        self.projects_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.projects_tree.setObjectName("projects_tree")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.projects_tree.headerItem().setFont(0, font)
        self.projects_tree.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.projects_tree.headerItem().setTextAlignment(
            3, QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.projects_tree, 3, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pull_all = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pull_all.sizePolicy().hasHeightForWidth())
        self.pull_all.setSizePolicy(sizePolicy)
        self.pull_all.setObjectName("pull_all")
        self.horizontalLayout_3.addWidget(self.pull_all)
        spacerItem1 = QtWidgets.QSpacerItem(
            280, 34, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.over_ride = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.over_ride.sizePolicy().hasHeightForWidth())
        self.over_ride.setSizePolicy(sizePolicy)
        self.over_ride.setObjectName("over_ride")
        self.horizontalLayout_3.addWidget(self.over_ride)
        self.debug_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.debug_checkbox.sizePolicy().hasHeightForWidth())
        self.debug_checkbox.setSizePolicy(sizePolicy)
        self.debug_checkbox.setObjectName("debug_checkbox")
        self.horizontalLayout_3.addWidget(self.debug_checkbox)
        self.open_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_3.addWidget(self.open_button)
        self.open_terminal = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.open_terminal.sizePolicy().hasHeightForWidth())
        self.open_terminal.setSizePolicy(sizePolicy)
        self.open_terminal.setIconSize(QtCore.QSize(16, 16))
        self.open_terminal.setFlat(True)
        self.open_terminal.setObjectName("open_terminal")
        self.horizontalLayout_3.addWidget(self.open_terminal)
        self.open_explorer = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.open_explorer.sizePolicy().hasHeightForWidth())
        self.open_explorer.setSizePolicy(sizePolicy)
        self.open_explorer.setFlat(True)
        self.open_explorer.setObjectName("open_explorer")
        self.horizontalLayout_3.addWidget(self.open_explorer)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)
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
        MainWindow.setTabOrder(self.search_bar, self.projects_tree)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quetzal"))
        self.search_bar.setToolTip(_translate(
            "MainWindow", "Filter projects by name or location"))
        self.error_display.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#212121;\">Hi!</span></p></body></html>"))
        self.projects_tree.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.projects_tree.headerItem().setText(1, _translate("MainWindow", "Location"))
        self.projects_tree.headerItem().setText(
            2, _translate("MainWindow", "Favorited"))
        self.projects_tree.headerItem().setText(3, _translate("MainWindow", "Due Date"))
        self.pull_all.setToolTip(_translate(
            "MainWindow", "Update All Watched Projects"))
        self.pull_all.setText(_translate("MainWindow", "Update All"))
        self.over_ride.setToolTip(_translate(
            "MainWindow", "Updated projects will overwrite current ones"))
        self.over_ride.setText(_translate("MainWindow", "Override"))
        self.debug_checkbox.setToolTip(_translate(
            "MainWindow", "Open or Update in Debug Mode"))
        self.debug_checkbox.setText(_translate("MainWindow", "Debug"))
        self.open_button.setToolTip(_translate(
            "MainWindow", "Open Local Editor"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.open_terminal.setToolTip(_translate(
            "MainWindow", "Open Terminal In Project Directory"))
        self.open_terminal.setText(_translate("MainWindow", ">_"))
        self.open_explorer.setToolTip(_translate(
            "MainWindow", "Open in File Explorer"))
        self.open_explorer.setText(_translate("MainWindow", u"\U0001F4C2"))
        self.menuProjects.setTitle(_translate("MainWindow", "Projects"))
        self.menuLocations.setTitle(_translate("MainWindow", "Locations"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuQuetzal.setTitle(_translate("MainWindow", "Quetzal"))
        self.actionCreate_New.setText(_translate("MainWindow", "Create New"))
        self.actionCreate_New.setToolTip(
            _translate("MainWindow", "Clone a new project"))
        self.actionAdd_Project_Path.setText(
            _translate("MainWindow", "Add Project Path"))
        self.actionAdd_Project_Path.setToolTip(_translate(
            "MainWindow", "In case you  deleted one or Quetzal couldn\'t find it"))
        self.actionDelete_Project_Path.setText(
            _translate("MainWindow", "Delete Project Path"))
        self.actionAdd_Watched_Folder.setText(
            _translate("MainWindow", "Add Watched Folder"))
        self.actionAdd_Watched_Folder.setToolTip(_translate(
            "MainWindow", "Quetzal will look for projects in these folders"))
        self.actionRemove_Watched_Folder.setText(
            _translate("MainWindow", "Remove Watched Folder"))
        self.actionChange_Main_Folder.setText(
            _translate("MainWindow", "Change Main Folder"))
        self.actionChange_Main_Folder.setToolTip(_translate(
            "MainWindow", "Your new cloned projects will be created here"))
        self.actionChange_Settings.setText(
            _translate("MainWindow", "Settings"))
        self.actionChange_Settings.setToolTip(_translate(
            "MainWindow", "Change the way Quetzal looks and behaves"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setToolTip(_translate(
            "MainWindow", "Rescan your device for project files"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setToolTip(_translate(
            "MainWindow", "Refreshes the status of all projects"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
