# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Confirm_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Confirm_Dialog(QtWidgets.QDialog):
    def __init__(self, slug):
        super(Ui_Confirm_Dialog, self).__init__()
        self.slug = slug

    def setupUi(self, Confirm_Dialog):
        Confirm_Dialog.setObjectName("Confirm_Dialog")
        Confirm_Dialog.resize(300, 140)
        Confirm_Dialog.setStyleSheet("""
                                QWidget{ font: 75 11pt \"Noto Sans\"; }

                                QWidget#centralwidget {
                                    background-color: #f5f6f7;
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

                                QLabel {
                                    font-weight: 500;
                                    color: #434348;
                                }
                                """)
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
        self.prompt.setText(_translate(
            "Confirm_Dialog", f"Are you sure you want to remove {self.slug}?"))
