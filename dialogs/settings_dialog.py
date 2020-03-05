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
from quetzal import projects, write


def validJson(plain_text):
    try:
        json.dumps(plain_text)
        return True
    except:
        return False


class Ui_Settings_Dialog(QtWidgets.QDialog):
    def __init__(self, params):
        super().__init__()
        self.setStyleSheet(STYLES())
        self.params = params
        self.new_conf = {}
        self.last_color = params['highlight_color']
        self.last_font = params['font']
        self.new_font = {'family': '', 'size': ''}
        self.new_color = ""
        self.new_json = ""
        self.re_styles = {}

    def returnVal(self):
        self.re_styles = {
            'font': {
                'pre_size': self.last_font['size'],
                'pre_fam': self.last_font['family'],
                'post_size': self.new_font['size'],
                'post_fam': self.new_font['family']
            },
            'color': {
                'prev': self.last_color,
                'new': self.new_color
            }
        }

        curr_vals = {
            'terminal': self.terminal_input.text(),
            'text_editor': self.editor_input.text(),
            'update_on_start': str(self.refresh_on_start.isChecked()),
            'highlight_color': self.re_styles['color']['new'],
            'font': {
                'size': self.new_font['size'],
                'family': self.new_font['family']
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
        self.new_font['family'] = new_font.toString().split(',')[0]
        self.font_display.setStyleSheet(
            f"font-family: {self.new_font['family']};font-size: {self.new_font['size']};")
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
            write(self.new_json)

    def confirmDialog(self):
        dialog = QtWidgets.QDialog()
        message = "Are you sure you want to make these changes to your JSON? Bad format can break app functionality."
        dialog.ui = Ui_Confirm_Dialog(message)
        dialog.ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            return True
        return False

    def setupUi(self, Settings_Dialog):
        Settings_Dialog.setObjectName("Settings_Dialog")
        Settings_Dialog.resize(543, 301)
        self.widget = QtWidgets.QWidget(Settings_Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 521, 281))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.styles_editor = QtWidgets.QTabWidget(self.widget)
        self.styles_editor.setObjectName("styles_editor")
        self.basic_settings = QtWidgets.QWidget()
        self.basic_settings.setObjectName("basic_settings")
        self.terminal_input = QtWidgets.QLineEdit(self.basic_settings)
        self.terminal_input.setGeometry(QtCore.QRect(10, 30, 359, 33))
        self.terminal_input.setObjectName("terminal_input")
        self.terminal_input.textChanged.connect(self.returnVal)
        if self.params['terminal'] != 'none':
            self.terminal_input.setPlaceholderText(self.params['terminal'])
        else:
            self.terminal_input.setPlaceholderText('')

        self.editor_input = QtWidgets.QLineEdit(self.basic_settings)
        self.editor_input.setGeometry(QtCore.QRect(10, 90, 359, 33))
        self.editor_input.setObjectName("editor_input")
        self.editor_input.textChanged.connect(self.returnVal)
        if self.params['text_editor'] != 'none':
            self.editor_input.setPlaceholderText(self.params['text_editor'])
        else:
            self.editor_input.setPlaceholderText('')

        self.terminal_label = QtWidgets.QLabel(self.basic_settings)
        self.terminal_label.setGeometry(QtCore.QRect(10, 10, 359, 17))
        self.terminal_label.setObjectName("terminal_label")
        self.editor_label = QtWidgets.QLabel(self.basic_settings)
        self.editor_label.setGeometry(QtCore.QRect(10, 70, 359, 17))
        self.editor_label.setObjectName("editor_label")
        self.refresh_on_start = QtWidgets.QCheckBox(self.basic_settings)
        self.refresh_on_start.setGeometry(QtCore.QRect(10, 140, 359, 23))
        self.refresh_on_start.setObjectName("refresh_on_start")
        if self.params['update_on_start'] == 'True':
            self.refresh_on_start.setChecked(True)
        self.refresh_on_start.stateChanged.connect(self.returnVal)

        self.styles_editor.addTab(self.basic_settings, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget1 = QtWidgets.QWidget(self.tab_3)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 235, 181))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.font_label_3 = QtWidgets.QLabel(self.widget1)
        self.font_label_3.setObjectName("font_label_3")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.font_label_3)
        self.font_dropdown = QtWidgets.QFontComboBox(self.widget1)
        self.font_dropdown.setObjectName("font_dropdown")
        if self.params['font']['family'] != 'none':
            self.font_dropdown.setCurrentFont(
                QtGui.QFont(self.params['font']['family']))
        self.font_dropdown.currentFontChanged.connect(self.fontPreview)

        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.font_dropdown)
        spacerItem = QtWidgets.QSpacerItem(
            20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            2, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.font_size_label = QtWidgets.QLabel(self.widget1)
        self.font_size_label.setObjectName("font_size_label")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.font_size_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            5, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.palette_label = QtWidgets.QLabel(self.widget1)
        self.palette_label.setObjectName("palette_label")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.palette_label)
        self.palette_trigger = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.palette_trigger.sizePolicy().hasHeightForWidth())
        self.palette_trigger.setSizePolicy(sizePolicy)
        self.palette_trigger.setObjectName("palette_trigger")
        self.palette_trigger.clicked.connect(self.colorDialog)

        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.palette_trigger)
        self.font_size_slider = QtWidgets.QSlider(self.widget1)
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

        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.font_size_slider)
        self.widget2 = QtWidgets.QWidget(self.tab_3)
        self.widget2.setGeometry(QtCore.QRect(257, 10, 251, 180))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.font_display = QtWidgets.QPlainTextEdit(self.widget2)
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
        self.highlight_color_display = QtWidgets.QFrame(self.widget2)
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
        self.styles_editor.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.direct_edit_stack = QtWidgets.QStackedWidget(self.tab_2)
        self.direct_edit_stack.setGeometry(QtCore.QRect(10, 10, 491, 181))
        self.direct_edit_stack.setObjectName("direct_edit_stack")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.key_bindings_editor = QtWidgets.QPlainTextEdit(self.page_3)
        self.key_bindings_editor.setGeometry(QtCore.QRect(0, 30, 491, 151))
        self.key_bindings_editor.setObjectName("key_bindings_editor")
        self.key_bindings_label = QtWidgets.QLabel(self.page_3)
        self.key_bindings_label.setGeometry(QtCore.QRect(10, 0, 359, 17))
        self.key_bindings_label.setObjectName("key_bindings_label")
        self.direct_edit_stack.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.json_editor = QtWidgets.QPlainTextEdit(self.page)
        self.json_editor.setGeometry(QtCore.QRect(0, 30, 491, 151))
        self.json_editor.setObjectName("json_editor")
        self.json_editor.setPlainText(json.dumps(projects()))
        self.json_editor.textChanged.connect(self.jsonChange)

        self.json_label = QtWidgets.QLabel(self.page)
        self.json_label.setGeometry(QtCore.QRect(10, 0, 359, 17))
        self.json_label.setObjectName("json_label")
        self.direct_edit_stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.style_editor = QtWidgets.QPlainTextEdit(self.page_2)
        self.style_editor.setGeometry(QtCore.QRect(0, 30, 491, 151))
        self.style_editor.setObjectName("style_editor")
        self.style_editor.setPlainText(STYLES())

        self.style_label = QtWidgets.QLabel(self.page_2)
        self.style_label.setGeometry(QtCore.QRect(10, 0, 359, 17))
        self.style_label.setObjectName("style_label")
        self.direct_edit_stack.addWidget(self.page_2)
        self.styles_editor.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.styles_editor, 0, 0, 1, 1)
        self.ok_cancel = QtWidgets.QDialogButtonBox(self.widget)
        self.ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel.setStandardButtons(
            QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel)
        self.ok_cancel.setObjectName("ok_cancel")
        self.gridLayout.addWidget(self.ok_cancel, 1, 0, 1, 1)

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

        self.retranslateUi(Settings_Dialog)
        self.styles_editor.setCurrentIndex(0)
        self.direct_edit_stack.setCurrentIndex(0)
        self.ok_cancel.accepted.connect(conditionalAccept)
        self.ok_cancel.rejected.connect(Settings_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings_Dialog)

    def retranslateUi(self, Settings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Settings_Dialog.setWindowTitle(_translate(
            "Settings_Dialog", "Quetzal Settings"))
        self.terminal_label.setText(_translate(
            "Settings_Dialog", "Open Terminal Command"))
        self.editor_label.setText(_translate(
            "Settings_Dialog", "Open Editor Command"))
        self.refresh_on_start.setText(
            _translate("Settings_Dialog", "Refresh on start"))
        self.styles_editor.setTabText(self.styles_editor.indexOf(
            self.basic_settings), _translate("Settings_Dialog", "Configuration"))
        self.font_label_3.setText(_translate(
            "Settings_Dialog", "Change App Font"))
        self.font_size_label.setText(_translate(
            "Settings_Dialog", "Change Font Size"))
        self.palette_label.setText(_translate(
            "Settings_Dialog", "Change Highlight Color"))
        self.palette_trigger.setText(
            _translate("Settings_Dialog", u"\U0001F3A8"))
        self.styles_editor.setTabText(self.styles_editor.indexOf(
            self.tab_3), _translate("Settings_Dialog", "Look and Feel"))
        self.key_bindings_label.setText(
            _translate("Settings_Dialog", "Key Bindings"))
        self.json_label.setText(_translate("Settings_Dialog", "JSON Editor"))
        self.style_label.setText(_translate("Settings_Dialog", "Style Editor"))
        self.styles_editor.setTabText(self.styles_editor.indexOf(
            self.tab_2), _translate("Settings_Dialog", "Advanced"))
