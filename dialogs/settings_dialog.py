# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import json
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogs.confirm_dialog import Ui_Confirm_Dialog
from get_styles import STYLES
from set_styles import setCustomStyles
from quetzal import qzWrite
from threading import Timer


def validJson(plain_text):
    try:
        json.dumps(plain_text)
        return True
    except:
        return False


def formatJson():
    with open('projects.json', 'r') as curr_json:
        lines = curr_json.read()
        return lines


class Ui_Settings_Dialog(QtWidgets.QDialog):
    def __init__(self, params):
        super().__init__()
        self.setStyleSheet(STYLES())
        self.params = params
        self.new_conf = {}
        self.last_color = params['highlight_color']
        self.last_font = params['font']
        self.new_font = {'fam': '', 'size': ''}
        self.new_color = ""
        self.new_json = ""
        self.re_styles = {}
        self.init_styles_text = STYLES()

    def returnVal(self):
        self.re_styles = {
            'font': {
                'size': self.new_font['size'],
                'fam': self.new_font['fam']
            },
            'color': self.new_color
        }

        curr_vals = {
            'terminal': self.terminal_input.text(),
            'text_editor': self.editor_input.text(),
            'update_on_start': str(self.refresh_on_start.isChecked()),
            'highlight_color': self.re_styles['color'],
            'font': {
                'size': self.new_font['size'],
                'family': self.new_font['fam']
            }
        }

        for key, val in curr_vals.items():
            if isinstance(val, str) and val != '':
                self.new_conf[key] = val
            elif key in {**curr_vals}:
                try:
                    del self.new_conf[key]
                except KeyError:
                    continue

    def fontPreview(self):
        new_font = self.font_dropdown.currentFont()
        self.new_font['size'] = f"{self.font_size_slider.value()}pt"
        self.new_font['fam'] = new_font.toString().split(',')[0]
        self.font_display.setStyleSheet(
            f"font-family: {self.new_font['fam']};font-size: {self.new_font['size']};")
        self.returnVal()

    def colorDialog(self):
        new_color = QtWidgets.QColorDialog.getColor()
        if new_color.isValid():
            self.new_color = str(new_color.name())
            self.highlight_color_display.setStyleSheet(
                f"background-color: {self.new_color};")
        self.returnVal()

    def jsonChange(self):
        self.new_json = self.json_editor.toPlainText()

    def jsonSet(self):
        if validJson(self.new_json) and self.confirmDialog():
            qzWrite(self.new_json)

    def confirmDialog(self):
        dialog = QtWidgets.QDialog()
        message = "Are you sure you want to make these changes to your JSON? Bad format can break app functionality."
        dialog.ui = Ui_Confirm_Dialog(message)
        dialog.ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            return True
        return False

    def tabChange(self):
        _index_ = self.tab_selector.currentText().lower()
        if "json" in _index_:
            self.direct_edit_stack.setCurrentWidget(self.json_editor_page)
        elif "style" in _index_:
            self.direct_edit_stack.setCurrentWidget(self.style_editor_page)
        elif "key" in _index_:
            self.direct_edit_stack.setCurrentWidget(self.key_bindings_page)
        else:
            return False

    def setupUi(self, Settings_Dialog):
        Settings_Dialog.setObjectName("Settings_Dialog")
        Settings_Dialog.resize(558, 318)
        Settings_Dialog.setStyleSheet(STYLES())
        self.gridLayout_2 = QtWidgets.QGridLayout(Settings_Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.settings_tabs = QtWidgets.QTabWidget(Settings_Dialog)
        self.settings_tabs.setObjectName("settings_tabs")
        self.basic_settings = QtWidgets.QWidget()
        self.basic_settings.setObjectName("basic_settings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.basic_settings)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.terminal_label = QtWidgets.QLabel(self.basic_settings)
        self.terminal_label.setObjectName("terminal_label")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.terminal_label)
        self.terminal_input = QtWidgets.QLineEdit(self.basic_settings)
        self.terminal_input.setObjectName("terminal_input")
        self.terminal_input.textChanged.connect(self.returnVal)
        if self.params['terminal'] != 'none':
            self.terminal_input.setPlaceholderText(self.params['terminal'])
        else:
            self.terminal_input.setPlaceholderText('')

        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.terminal_input)
        self.editor_label = QtWidgets.QLabel(self.basic_settings)
        self.editor_label.setObjectName("editor_label")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.editor_label)
        self.editor_input = QtWidgets.QLineEdit(self.basic_settings)
        self.editor_input.setObjectName("editor_input")
        self.editor_input.textChanged.connect(self.returnVal)
        if self.params['text_editor'] != 'none':
            self.editor_input.setPlaceholderText(self.params['text_editor'])
        else:
            self.editor_input.setPlaceholderText('')

        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.editor_input)
        self.refresh_on_start = QtWidgets.QCheckBox(self.basic_settings)
        self.refresh_on_start.setObjectName("refresh_on_start")
        if self.params['update_on_start'] == 'True':
            self.refresh_on_start.setChecked(True)
        self.refresh_on_start.stateChanged.connect(self.returnVal)
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.refresh_on_start)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.settings_tabs.addTab(self.basic_settings, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.font_label_3 = QtWidgets.QLabel(self.tab_3)
        self.font_label_3.setObjectName("font_label_3")
        self.verticalLayout_2.addWidget(self.font_label_3)
        self.font_dropdown = QtWidgets.QFontComboBox(self.tab_3)
        self.font_dropdown.setObjectName("font_dropdown")
        if self.params['font']['family'] != 'none':
            self.font_dropdown.setCurrentFont(
                QtGui.QFont(self.params['font']['family']))
        self.font_dropdown.currentFontChanged.connect(self.fontPreview)

        self.verticalLayout_2.addWidget(self.font_dropdown)
        spacerItem = QtWidgets.QSpacerItem(
            20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.font_size_label = QtWidgets.QLabel(self.tab_3)
        self.font_size_label.setObjectName("font_size_label")
        self.verticalLayout_2.addWidget(self.font_size_label)
        self.font_size_slider = QtWidgets.QSlider(self.tab_3)
        self.font_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.font_size_slider.setObjectName("font_size_slider")
        self.font_size_slider.setMinimum(9)
        self.font_size_slider.setMaximum(18)
        self.font_size_slider.setSingleStep(1)
        if self.last_font['size'] != 'none':
            size_val = int(
                self.last_font['size'].strip().replace('pt', ''))
            self.font_size_slider.setValue(size_val)
        else:
            self.font_size_slider.setValue(11)
        self.font_size_slider.valueChanged.connect(self.fontPreview)

        self.verticalLayout_2.addWidget(self.font_size_slider)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.palette_label = QtWidgets.QLabel(self.tab_3)
        self.palette_label.setObjectName("palette_label")
        self.verticalLayout_2.addWidget(self.palette_label)
        self.palette_trigger = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.palette_trigger.sizePolicy().hasHeightForWidth())
        self.palette_trigger.setSizePolicy(sizePolicy)
        self.palette_trigger.setObjectName("palette_trigger")
        self.palette_trigger.clicked.connect(self.colorDialog)

        self.verticalLayout_2.addWidget(self.palette_trigger)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.font_display = QtWidgets.QPlainTextEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(
            self.font_display.sizePolicy().hasHeightForWidth())
        self.font_display.setSizePolicy(sizePolicy)
        self.font_display.setObjectName("font_display")
        self.font_display.setStyleSheet(
            f"font-family: {self.last_font['family']};font-size: {self.last_font['size']};")
        self.font_display.setPlainText('Test new font here')

        self.verticalLayout.addWidget(self.font_display)
        self.highlight_color_display = QtWidgets.QFrame(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.highlight_color_display.sizePolicy().hasHeightForWidth())
        self.highlight_color_display.setSizePolicy(sizePolicy)
        self.highlight_color_display.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.highlight_color_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.highlight_color_display.setObjectName("highlight_color_display")
        self.highlight_color_display.setStyleSheet(
            f"background-color: {self.last_color};")

        self.verticalLayout.addWidget(self.highlight_color_display)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.settings_tabs.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tab_selector = QtWidgets.QComboBox(self.tab_2)
        self.tab_selector.setObjectName("tab_selector")
        self.tab_selector.addItem("")
        self.tab_selector.addItem("")
        self.tab_selector.addItem("")
        self.tab_selector.currentIndexChanged.connect(self.tabChange)

        self.gridLayout_4.addWidget(self.tab_selector, 0, 0, 1, 1)
        self.direct_edit_stack = QtWidgets.QStackedWidget(self.tab_2)
        self.direct_edit_stack.setObjectName("direct_edit_stack")
        self.key_bindings_page = QtWidgets.QWidget()
        self.key_bindings_page.setObjectName("key_bindings_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.key_bindings_page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.key_bindings_editor = QtWidgets.QPlainTextEdit(
            self.key_bindings_page)
        self.key_bindings_editor.setObjectName("key_bindings_editor")
        self.gridLayout_7.addWidget(self.key_bindings_editor, 0, 0, 1, 1)
        self.direct_edit_stack.addWidget(self.key_bindings_page)
        self.json_editor_page = QtWidgets.QWidget()
        self.json_editor_page.setObjectName("json_editor_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.json_editor_page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.json_editor = QtWidgets.QPlainTextEdit(self.json_editor_page)
        self.json_editor.setObjectName("json_editor")
        self.json_editor.setPlainText(formatJson())
        self.json_editor.textChanged.connect(self.jsonChange)

        self.gridLayout_5.addWidget(self.json_editor, 0, 0, 1, 1)
        self.direct_edit_stack.addWidget(self.json_editor_page)
        self.style_editor_page = QtWidgets.QWidget()
        self.style_editor_page.setObjectName("style_editor_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.style_editor_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.style_editor = QtWidgets.QPlainTextEdit(self.style_editor_page)
        self.style_editor.setObjectName("style_editor")

        self.gridLayout_6.addWidget(self.style_editor, 0, 0, 1, 1)
        self.direct_edit_stack.addWidget(self.style_editor_page)
        self.gridLayout_4.addWidget(self.direct_edit_stack, 1, 0, 1, 1)
        self.settings_tabs.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.settings_tabs, 0, 0, 1, 1)
        self.ok_cancel = QtWidgets.QDialogButtonBox(Settings_Dialog)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.gridLayout.addWidget(self.ok_cancel, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        def conditionalAccept():
            if len(self.new_json) > 0:
                if self.confirmDialog():
                    self.jsonSet()
                    return Settings_Dialog.accept()
                return Settings_Dialog.reject()
            else:
                setCustomStyles(
                    self.re_styles['font'], self.re_styles['color'])
                Settings_Dialog.accept()

        self.style_editor.setPlainText(self.init_styles_text)
        self.retranslateUi(Settings_Dialog)
        self.settings_tabs.setCurrentIndex(0)
        self.direct_edit_stack.setCurrentIndex(0)
        self.ok_cancel.accepted.connect(conditionalAccept)
        self.ok_cancel.rejected.connect(Settings_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings_Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quetzal Settings"))
        self.terminal_label.setText(_translate(
            "Dialog", "Open Terminal Command"))
        self.editor_label.setText(_translate("Dialog", "Open Editor Command"))
        self.refresh_on_start.setText(
            _translate("Dialog", "Refresh on start"))
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(
            self.basic_settings), _translate("Dialog", "Configuration"))
        self.font_label_3.setText(_translate("Dialog", "Change App Font"))
        self.font_size_label.setText(_translate("Dialog", "Change Font Size"))
        self.palette_label.setText(_translate(
            "Dialog", "Change Highlight Color"))
        self.palette_trigger.setText(_translate("Dialog", u"\U0001F3A8"))
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(
            self.tab_3), _translate("Dialog", "Look and Feel"))
        self.tab_selector.setItemText(0, _translate("Dialog", "Style Editor"))
        self.tab_selector.setItemText(1, _translate("Dialog", "JSON Editor"))
        self.tab_selector.setItemText(2, _translate("Dialog", "Key Bindings"))
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(
            self.tab_2), _translate("Dialog", "Advanced"))
