# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

STYLE = """
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
        color: #434348;
    }
    """


class Ui_Settings_Dialog(QtWidgets.QDialog):
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.new_conf = {}
        self.color_selection = params['highlight_color']
        self.font_selection = params['font']

    def returnVal(self):
        curr_vals = {
            'terminal': self.terminal_input.text(),
            'font': self.font_selection,
            'highlight_color': self.color_selection,
            'auto_start': str(self.refresh_on_start.isChecked())
        }

        for key, val in curr_vals.items():
            if isinstance(val, str) and val != "":
                self.new_conf[key] = val
            elif key in {**curr_vals}:
                try:
                    del self.new_conf[key]
                except KeyError:
                    continue

    def fontPreview(self):
        new_font = self.font_dropdown.currentFont()
        self.font_selection = new_font.toString().split(',')[0]
        self.returnVal()

    def colorDialog(self):
        new_color = QtWidgets.QColorDialog.getColor()
        if new_color.isValid():
            self.color_selection = str(new_color.name())
        self.returnVal()

    def setupUi(self, Settings_Dialog):
        Settings_Dialog.setObjectName("Settings_Dialog")
        Settings_Dialog.resize(400, 278)
        Settings_Dialog.setStyleSheet(
            "QWidget{ font: 75 11pt \"Noto Sans\"; }" + STYLE)
        self.layoutWidget = QtWidgets.QWidget(Settings_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.terminal_label = QtWidgets.QLabel(self.layoutWidget)
        self.terminal_label.setObjectName("terminal_label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.terminal_label)
        self.terminal_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.terminal_input.setObjectName("terminal_input")
        self.terminal_input.textChanged.connect(self.returnVal)
        self.terminal_input.setPlaceholderText(self.params['terminal'])

        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.terminal_input)
        self.font_dropdown = QtWidgets.QFontComboBox(self.layoutWidget)
        self.font_dropdown.setObjectName("font_dropdown")
        if self.params['font'] != 'none':
            self.font_dropdown.setCurrentFont(QtGui.QFont(self.params['font']))
        self.font_dropdown.currentFontChanged.connect(self.fontPreview)

        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.font_dropdown)
        spacerItem = QtWidgets.QSpacerItem(
            20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            5, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.app_color = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.app_color.sizePolicy().hasHeightForWidth())
        self.app_color.setSizePolicy(sizePolicy)
        self.app_color.setObjectName("app_color")
        self.app_color.clicked.connect(self.colorDialog)

        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.SpanningRole, self.app_color)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            7, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.refresh_on_start = QtWidgets.QCheckBox(self.layoutWidget)
        self.refresh_on_start.setObjectName("refresh_on_start")
        self.refresh_on_start.stateChanged.connect(self.returnVal)
        if self.params['auto_start'] == 'True':
            self.refresh_on_start.setChecked(True)

        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.LabelRole, self.refresh_on_start)
        self.ok_cancel = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.ok_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            2, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.font_label = QtWidgets.QLabel(self.layoutWidget)
        self.font_label.setObjectName("font_label")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.font_label)

        self.retranslateUi(Settings_Dialog)
        self.ok_cancel.accepted.connect(Settings_Dialog.accept)
        self.ok_cancel.rejected.connect(Settings_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings_Dialog)

    def retranslateUi(self, Settings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Settings_Dialog.setWindowTitle(_translate(
            "Settings_Dialog", "Quetzal Settings"))
        self.terminal_label.setText(_translate(
            "Settings_Dialog", "Open Terminal Command"))
        self.app_color.setText(_translate(
            "Settings_Dialog", "Change App Highlight Color"))
        self.refresh_on_start.setText(_translate(
            "Settings_Dialog", "Refresh on start"))
        self.font_label.setText(_translate(
            "Settings_Dialog", "Change App Font"))
