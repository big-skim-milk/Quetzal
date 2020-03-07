# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from get_styles import STYLES
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cal_Dialog(QtWidgets.QDialog):
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.date_val = ""

    def return_val(self):
        date_choice = self.cal_widget.selectedDate().toString("dd MM yyyy")
        time_choice = self.time_widget.time().toString("H:mm")

        if date_choice:
            if time_choice:
                self.date_val = f"{date_choice}, {time_choice}"
            else:
                self.date_val = f"{date_choice}"
        else:
            self.date_val = ""

    def setupUi(self, Cal_Dialog):
        Cal_Dialog.setObjectName("Cal_Dialog")
        Cal_Dialog.resize(532, 299)
        self.gridLayout = QtWidgets.QGridLayout(Cal_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cal_widget = QtWidgets.QCalendarWidget(Cal_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(
            self.cal_widget.sizePolicy().hasHeightForWidth())
        self.cal_widget.setSizePolicy(sizePolicy)
        self.cal_widget.setObjectName("cal_widget")
        self.cal_widget.setMinimumDate(QtCore.QDate.currentDate())
        self.cal_widget.selectionChanged.connect(self.return_val)
        if self.params['set_date'] != '':
            D = [int(d) for d in self.params['set_date'].split(' ')]
            self.cal_widget.setSelectedDate(
                QtCore.QDate(D[2], D[1], D[0]))

        self.gridLayout_2.addWidget(self.cal_widget, 0, 0, 1, 2)
        self.time_widget = QtWidgets.QTimeEdit(Cal_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.time_widget.sizePolicy().hasHeightForWidth())
        self.time_widget.setSizePolicy(sizePolicy)
        self.time_widget.setObjectName("time_widget")
        self.time_widget.timeChanged.connect(self.return_val)
        if self.params['set_time'] != '':
            T = [int(t) for t in self.params['set_time'].strip().split(':')]
            self.time_widget.setTime(QtCore.QTime(T[0], T[1]))

        self.gridLayout_2.addWidget(self.time_widget, 2, 0, 1, 1)
        self.ok_cancel = QtWidgets.QDialogButtonBox(Cal_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.ok_cancel.sizePolicy().hasHeightForWidth())
        self.ok_cancel.setSizePolicy(sizePolicy)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.gridLayout_2.addWidget(self.ok_cancel, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Cal_Dialog)
        self.ok_cancel.accepted.connect(Cal_Dialog.accept)
        self.ok_cancel.rejected.connect(Cal_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Cal_Dialog)

    def retranslateUi(self, Cal_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Cal_Dialog.setWindowTitle(_translate(
            "Cal_Dialog", f"Set Deadline for {self.params['name']}"))
