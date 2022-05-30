from PyQt5 import QtCore, QtGui, QtWidgets
from generate import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Main window
        icon = QtGui.QIcon()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(100, 100, 800, 400)
        MainWindow.setWindowTitle("imPASSible")
        MainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        #Title and welcome
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 30, 800, 50))
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(0, 100, 800, 30))
        font.setPointSize(16)
        self.text1.setFont(font)
        self.text1.setAlignment(QtCore.Qt.AlignCenter)

        #Generated password
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(50, 150, 700, 25))
        self.linePassword.setFont(font)
        self.linePassword.setFrame(True)
        self.linePassword.setReadOnly(True)
        self.linePassword.setAlignment(QtCore.Qt.AlignCenter)

        #Generate button
        self.buttonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerate.setGeometry(QtCore.QRect(200, 200, 200, 25))
        font.setPointSize(11)
        self.buttonGenerate.setFont(font)

        self.buttonCopy = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCopy.setGeometry(QtCore.QRect(400, 200, 200, 25))
        self.buttonCopy.setFont(font)

        #Credit
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect())
        self.text2.setGeometry(QtCore.QRect(0, 330, 800, 30))
        font.setPointSize(9)
        self.text2.setFont(font)
        self.text2.setAlignment(QtCore.Qt.AlignCenter)


        #Language change
        self.english = QtWidgets.QPushButton(self.centralwidget)
        self.english.setGeometry(QtCore.QRect(310, 270, 80, 40))
        icon.addPixmap(QtGui.QPixmap("img/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.english.setIcon(icon)
        self.english.setIconSize(QtCore.QSize(80, 40))

        self.turkish = QtWidgets.QPushButton(self.centralwidget)
        self.turkish.setGeometry(QtCore.QRect(410, 270, 80, 40))
        icon.addPixmap(QtGui.QPixmap("img/turkish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turkish.setIcon(icon)
        self.turkish.setIconSize(QtCore.QSize(80, 40))


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow, "en")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonGenerate.clicked.connect(self.generating)
        self.buttonCopy.clicked.connect(self.copying)
        self.english.clicked.connect(lambda: self.retranslateUi(MainWindow, "en"))
        self.turkish.clicked.connect(lambda: self.retranslateUi(MainWindow, "tr"))


    def retranslateUi(self, MainWindow, lang):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("MainWindow", "imPASSible"))
        self.text1.setText(_translate("MainWindow", "Generate a strong password!" if lang == "en" else "Güçlü bir şifre oluştur!"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generate!" if lang == "en" else "Oluştur!"))
        self.buttonCopy.setText(_translate("MainWindow", "Copy" if lang == "en" else "Kopyala"))
        self.lang = lang
        self.text2.setText(_translate("MainWindow", "Oguz Alp Cakmak - Galatasaray University - 2022"))


    def generating(self):
        self.linePassword.setText(superset(3))


    def copying(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.linePassword.displayText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    font = QtGui.QFont()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
