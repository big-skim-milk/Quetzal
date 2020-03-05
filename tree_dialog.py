# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        Tree_Dialog.setStyleSheet("""
                                QWidget{ font: 75 11pt \"Noto Sans\"; }

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
                                    color: #00B554;
                                }

                                QMenuBar::item {
                                    background-color: transparent;
                                    color: #9F9EA5;
                                }

                                QMenuBar::item:selected {
                                    color: #434348;
                                }
                                """)
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
