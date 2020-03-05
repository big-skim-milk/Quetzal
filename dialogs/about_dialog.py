# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from get_styles import STYLES
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About_Dialog(QtWidgets.QDialog):
    def setupUi(self, About_Dialog):
        About_Dialog.setObjectName("About_Dialog")
        About_Dialog.resize(318, 209)
        About_Dialog.setStyleSheet(STYLES())
        self.widget = QtWidgets.QWidget(About_Dialog)
        self.widget.setGeometry(QtCore.QRect(26, 20, 261, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quetzal_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.quetzal_label.sizePolicy().hasHeightForWidth())
        self.quetzal_label.setSizePolicy(sizePolicy)
        self.quetzal_label.setStyleSheet("")
        self.quetzal_label.setScaledContents(False)
        self.quetzal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.quetzal_label.setWordWrap(True)
        self.quetzal_label.setOpenExternalLinks(True)
        self.quetzal_label.setObjectName("quetzal_label")
        self.verticalLayout.addWidget(self.quetzal_label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.close_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.close_button.setObjectName("close_button")
        self.verticalLayout.addWidget(
            self.close_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(About_Dialog)
        self.close_button.clicked.connect(About_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(About_Dialog)

    def retranslateUi(self, About_Dialog):
        _translate = QtCore.QCoreApplication.translate
        About_Dialog.setWindowTitle(
            _translate("About_Dialog", "About Quetzal"))
        self.quetzal_label.setText(_translate(
            "About_Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Quetzal </span><span style=\" font-size:12pt; font-weight:600;\">v0.1</span></p></body></html>"))
        self.label_2.setText(_translate("About_Dialog", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/wix-incubator/corvid\"><span style=\" font-size:12pt; text-decoration: underline; color:#2a76c6;\">Wix Local Editor</span></a><span style=\" font-size:12pt;\"> Projects Manager</span></p><p align=\"center\"><a href=\"https://github.com/big-skim-milk/Quetzal\"><span style=\" font-size:11pt; text-decoration: underline; color:#2a76c6;\">Main Page</span></a></p></body></html>"))
        self.close_button.setText(_translate("About_Dialog", "Close"))
