from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator
import html


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(107, 161, 161);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_translate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_translate.setGeometry(QtCore.QRect(230, 480, 360, 80))
        self.btn_translate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_translate.setStyleSheet("background-color: rgb(100, 207, 0);")
        self.btn_translate.setObjectName("btn_translate")
        self.rbtn_no_change = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_no_change.setGeometry(QtCore.QRect(40, 310, 82, 17))
        self.rbtn_no_change.setObjectName("rbtn_no_change")
        self.rbtnRU = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnRU.setGeometry(QtCore.QRect(40, 350, 82, 21))
        self.rbtnRU.setObjectName("rbtnRU")
        self.rbtnENG = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnENG.setGeometry(QtCore.QRect(40, 390, 82, 17))
        self.rbtnENG.setObjectName("rbtnENG")
        self.checkBox_BOLD = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_BOLD.setGeometry(QtCore.QRect(320, 310, 70, 17))
        self.checkBox_BOLD.setObjectName("checkBox_BOLD")
        self.checkBox_U = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_U.setGeometry(QtCore.QRect(320, 350, 70, 17))
        self.checkBox_U.setObjectName("checkBox_U")
        self.checkBox_I = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_I.setGeometry(QtCore.QRect(320, 390, 70, 17))
        self.checkBox_I.setObjectName("checkBox_I")
        self.checkBox_Style = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Style.setGeometry(QtCore.QRect(520, 320, 70, 17))
        self.checkBox_Style.setObjectName("checkBox_Style")
        self.checkBox_Link = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Link.setGeometry(QtCore.QRect(520, 370, 70, 17))
        self.checkBox_Link.setObjectName("checkBox_Link")
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(50, 10, 160, 220))
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 10, 160, 220))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(590, 10, 160, 220))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit_style = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_style.setGeometry(QtCore.QRect(590, 310, 160, 30))
        self.textEdit_style.setObjectName("textEdit_style")
        self.textEdit_link = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_link.setGeometry(QtCore.QRect(590, 360, 160, 30))
        self.textEdit_link.setObjectName("textEdit_link")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.press_btn_translate()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_translate.setText(_translate("MainWindow", "Press me"))
        self.rbtn_no_change.setText(_translate("MainWindow", "Не менять"))
        self.rbtnRU.setText(_translate("MainWindow", "RU"))
        self.rbtnENG.setText(_translate("MainWindow", "ENG"))
        self.checkBox_BOLD.setText(_translate("MainWindow", "BOLD"))
        self.checkBox_U.setText(_translate("MainWindow", "U"))
        self.checkBox_I.setText(_translate("MainWindow", "I"))
        self.checkBox_Style.setText(_translate("MainWindow", "Style"))
        self.checkBox_Link.setText(_translate("MainWindow", "Link"))
        self.textEdit_1.setPlaceholderText(_translate("MainWindow", "Enter your text..."))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Result"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "HTML structure"))
        self.textEdit_style.setPlaceholderText(_translate("MainWindow", "for example color: red"))
        self.textEdit_link.setPlaceholderText(_translate("MainWindow", "Write the address for your link"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Save as"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    def translate_text(self):
        text_to_translate = self.textEdit_1.toPlainText()
        translator = Translator()
        translated_text = ''
        if self.rbtnENG.isChecked():
            translated_text = translator.translate(text_to_translate, src='ru', dest='en').text
        elif self.rbtnRU.isChecked():
            translated_text = translator.translate(text_to_translate, src='en', dest='ru').text
        elif self.rbtn_no_change.isChecked():
            translated_text = text_to_translate

        if self.checkBox_BOLD.isChecked():
            translated_text = f"<b>{translated_text}</b>"
        if self.checkBox_U.isChecked():
            translated_text = f"<u>{translated_text}</u>"
        if self.checkBox_I.isChecked():
            translated_text = f"<i>{translated_text}</i>"

        if self.checkBox_Style.isChecked():
            style = self.textEdit_style.toPlainText().strip()
            if style:
                translated_text = f'<span style="{style}">{translated_text}</span>'

        if self.checkBox_Link.isChecked():
            link = self.textEdit_link.toPlainText().strip()
            if link:
                translated_text = f'<a href="{link}">{translated_text}</a>'

        self.textEdit_2.setText(translated_text)
        self.get_html()


    def get_html(self):
        html_structure = html.escape(self.textEdit_2.toHtml())
        self.textBrowser.setPlainText(html_structure)

    def press_btn_translate(self):
        self.btn_translate.clicked.connect(self.translate_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
