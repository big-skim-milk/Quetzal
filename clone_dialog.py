# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clone_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Clone_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Clone_Dialog, self).__init__()
        self.clone_params = {}

    def return_vals(self):
        if len(self.name_input.text()) > 0 and len(self.name_input.text()) > 6:
            self.clone_params = {
                'name': self.name_input.text(),
                'url': self.url_input.text(),
                'debug': self.do_debug.isChecked()
            }
        else:
            self.clone_params = {}

    def setupUi(self, Clone_Dialog):
        Clone_Dialog.setObjectName("Clone_Dialog")
        Clone_Dialog.resize(400, 225)
        Clone_Dialog.setStyleSheet("""
                                QWidget{ font: 75 12pt \"Noto Sans\"; }

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
                                    color: #434348;
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
                                    color: #00B554;
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
        self.widget = QtWidgets.QWidget(Clone_Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 341, 194))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.name_input = QtWidgets.QLineEdit(self.widget)
        self.name_input.setObjectName("name_input")
        self.name_input.textChanged.connect(self.return_vals)

        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.name_input)
        self.url_input = QtWidgets.QLineEdit(self.widget)
        self.url_input.setObjectName("url_input")
        self.url_input.textChanged.connect(self.return_vals)

        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.url_input)
        self.do_debug = QtWidgets.QCheckBox(self.widget)
        self.do_debug.setObjectName("do_debug")
        self.do_debug.stateChanged.connect(self.return_vals)

        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.do_debug)
        self.ok_cancel = QtWidgets.QDialogButtonBox(self.widget)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.ok_cancel)
        self.url_label = QtWidgets.QLabel(self.widget)
        self.url_label.setObjectName("url_label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.url_label)
        self.name_label = QtWidgets.QLabel(self.widget)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.name_label)

        self.retranslateUi(Clone_Dialog)
        self.ok_cancel.accepted.connect(Clone_Dialog.accept)
        self.ok_cancel.rejected.connect(Clone_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Clone_Dialog)

    def retranslateUi(self, Clone_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Clone_Dialog.setWindowTitle(_translate(
            "Clone_Dialog", "Clone New Project"))
        self.do_debug.setText(_translate("Clone_Dialog", "Debug Mode"))
        self.url_label.setText(_translate(
            "Clone_Dialog", "Site or Editor URL"))
        self.name_label.setText(_translate("Clone_Dialog", "New Project Name"))
