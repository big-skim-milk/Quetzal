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
        Cal_Dialog.setStyleSheet(STYLES())
        self.ok_cancel = QtWidgets.QDialogButtonBox(Cal_Dialog)
        self.ok_cancel.setGeometry(QtCore.QRect(170, 250, 341, 32))
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")

        self.cal_widget = QtWidgets.QCalendarWidget(Cal_Dialog)
        self.cal_widget.setGeometry(QtCore.QRect(10, 10, 501, 221))
        self.cal_widget.setObjectName("cal_widget")
        self.cal_widget.setMinimumDate(QtCore.QDate.currentDate())
        self.cal_widget.selectionChanged.connect(self.return_val)
        if self.params['set_date'] != '':
            D = [int(d) for d in self.params['set_date'].split(' ')]
            self.cal_widget.setSelectedDate(
                QtCore.QDate(D[2], D[1], D[0]))

        self.time_widget = QtWidgets.QTimeEdit(Cal_Dialog)
        self.time_widget.setGeometry(QtCore.QRect(30, 250, 221, 33))
        self.time_widget.setObjectName("time_widget")
        self.time_widget.timeChanged.connect(self.return_val)
        if self.params['set_time'] != '':
            T = [int(t) for t in self.params['set_time'].strip().split(':')]
            self.time_widget.setTime(QtCore.QTime(T[0], T[1]))

        self.retranslateUi(Cal_Dialog)
        self.ok_cancel.accepted.connect(Cal_Dialog.accept)
        self.ok_cancel.rejected.connect(Cal_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Cal_Dialog)

    def retranslateUi(self, Cal_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Cal_Dialog.setWindowTitle(_translate(
            "Cal_Dialog", f"Set Deadline for {self.params['name']}"))
