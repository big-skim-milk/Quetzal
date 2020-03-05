# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from get_styles import STYLES


class Ui_Tree_Dialog(QtWidgets.QDialog):
    def __init__(self, params):
        super(Ui_Tree_Dialog, self).__init__()
        self.params = params
        self.current_value = ''

    def return_val(self):
        self.current_value = self.tree_widget.currentItem().text(0) or ''

    def setupUi(self, Tree_Dialog):
        Tree_Dialog.setObjectName("Tree_Dialog")
        Tree_Dialog.resize(535, 270)
        Tree_Dialog.setStyleSheet(STYLES())
        self.widget = QtWidgets.QWidget(Tree_Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 491, 233))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.tree_widget = QtWidgets.QTreeWidget(self.widget)
        self.tree_widget.setObjectName("tree_widget")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.tree_widget)
        self.ok_cancel = QtWidgets.QDialogButtonBox(self.widget)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.ok_cancel)

        for key, val in self.params['data']:
            lx_item = QtWidgets.QTreeWidgetItem(self.tree_widget, [
                key,
                val
            ])

            if not key == "main":
                lx_item.setFlags(lx_item.flags() | 128 | 1)
            elif key == "main":
                lx_item.setFlags(lx_item.flags() | 128)

        self.tree_widget.currentItemChanged.connect(self.return_val)

        self.retranslateUi(Tree_Dialog)
        self.ok_cancel.accepted.connect(Tree_Dialog.accept)
        self.ok_cancel.rejected.connect(Tree_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Tree_Dialog)

    def retranslateUi(self, Tree_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Tree_Dialog.setWindowTitle(_translate(
            "Tree_Dialog", "Projects List Edit"))
        self.tree_widget.headerItem().setText(0, _translate("Tree_Dialog", "Name"))
        self.tree_widget.headerItem().setText(1, _translate("Tree_Dialog", "Location"))
