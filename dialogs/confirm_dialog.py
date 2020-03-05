# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Confirm_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from get_styles import STYLES


class Ui_Confirm_Dialog(QtWidgets.QDialog):
    def __init__(self, message):
        super(Ui_Confirm_Dialog, self).__init__()
        self.message = message

    def setupUi(self, Confirm_Dialog):
        Confirm_Dialog.setObjectName("Confirm_Dialog")
        Confirm_Dialog.resize(300, 140)
        Confirm_Dialog.setStyleSheet(STYLES())
        self.ok_cancel = QtWidgets.QDialogButtonBox(Confirm_Dialog)
        self.ok_cancel.setGeometry(QtCore.QRect(30, 90, 260, 32))
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.prompt = QtWidgets.QLabel(Confirm_Dialog)
        self.prompt.setGeometry(QtCore.QRect(15, 30, 270, 50))
        self.prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.prompt.setWordWrap(True)
        self.prompt.setObjectName("prompt")

        self.retranslateUi(Confirm_Dialog)
        self.ok_cancel.accepted.connect(Confirm_Dialog.accept)
        self.ok_cancel.rejected.connect(Confirm_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Confirm_Dialog)

    def retranslateUi(self, Confirm_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Confirm_Dialog.setWindowTitle(
            _translate("Confirm_Dialog", "Confirm Remove"))
        self.prompt.setText(_translate("Confirm_Dialog", self.message))
