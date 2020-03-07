# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clone_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from get_styles import STYLES


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
        Clone_Dialog.resize(400, 171)
        Clone_Dialog.setStyleSheet(STYLES())
        self.gridLayout = QtWidgets.QGridLayout(Clone_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.url_input = QtWidgets.QLineEdit(Clone_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.url_input.sizePolicy().hasHeightForWidth())
        self.url_input.setSizePolicy(sizePolicy)
        self.url_input.setObjectName("url_input")
        self.url_input.textChanged.connect(self.return_vals)

        self.gridLayout_2.addWidget(self.url_input, 1, 0, 1, 2)
        self.name_input = QtWidgets.QLineEdit(Clone_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy)
        self.name_input.setObjectName("name_input")
        self.name_input.textChanged.connect(self.return_vals)

        self.gridLayout_2.addWidget(self.name_input, 3, 0, 1, 2)
        self.do_debug = QtWidgets.QCheckBox(Clone_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.do_debug.sizePolicy().hasHeightForWidth())
        self.do_debug.setSizePolicy(sizePolicy)
        self.do_debug.setObjectName("do_debug")
        self.do_debug.stateChanged.connect(self.return_vals)

        self.gridLayout_2.addWidget(self.do_debug, 4, 0, 1, 1)
        self.ok_cancel = QtWidgets.QDialogButtonBox(Clone_Dialog)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.gridLayout_2.addWidget(self.ok_cancel, 4, 1, 1, 1)
        self.url_label = QtWidgets.QLabel(Clone_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.url_label.sizePolicy().hasHeightForWidth())
        self.url_label.setSizePolicy(sizePolicy)
        self.url_label.setObjectName("url_label")
        self.gridLayout_2.addWidget(self.url_label, 0, 0, 1, 2)
        self.name_label = QtWidgets.QLabel(Clone_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setObjectName("name_label")
        self.gridLayout_2.addWidget(self.name_label, 2, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

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
