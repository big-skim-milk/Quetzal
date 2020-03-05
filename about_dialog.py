# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About_Dialog(QtWidgets.QDialog):
    def setupUi(self, About_Dialog):
        About_Dialog.setObjectName("About_Dialog")
        About_Dialog.resize(310, 218)
        About_Dialog.setStyleSheet("""
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
        self.splitter = QtWidgets.QSplitter(About_Dialog)
        self.splitter.setGeometry(QtCore.QRect(50, 20, 205, 176))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setStyleSheet("")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.close_button = QtWidgets.QPushButton(self.splitter)
        self.close_button.setObjectName("close_button")

        self.retranslateUi(About_Dialog)
        self.close_button.clicked.connect(About_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(About_Dialog)

    def retranslateUi(self, About_Dialog):
        _translate = QtCore.QCoreApplication.translate
        About_Dialog.setWindowTitle(
            _translate("About_Dialog", "About Quetzal"))
        self.label.setText(_translate("About_Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Quetzal</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Wix Local Projects Manager</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">v0.1</span></p><p align=\"center\"><br/></p></body></html>"))
        self.close_button.setText(_translate("About_Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About_Dialog = QtWidgets.QDialog()
    ui = Ui_About_Dialog()
    ui.setupUi(About_Dialog)
    About_Dialog.show()
    sys.exit(app.exec_())
