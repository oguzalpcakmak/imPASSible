import sys
from icons import *
from pwdgen import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(315, 312)
        icon = QtGui.QIcon()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.set_en = QPushButton(self.centralwidget)
        self.set_en.setObjectName(u"set_en")
        icon.addPixmap(QtGui.QPixmap(en_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set_en.setIcon(icon)
        self.set_en.setIconSize(QtCore.QSize(80, 40))

        self.gridLayout.addWidget(self.set_en, 4, 0, 1, 1)

        self.linePwd = QLineEdit(self.centralwidget)
        self.linePwd.setObjectName(u"linePwd")
        self.linePwd.setAlignment(Qt.AlignCenter)
        self.linePwd.setReadOnly(True)

        self.gridLayout.addWidget(self.linePwd, 2, 0, 1, 2)

        self.signature = QLabel(self.centralwidget)
        self.signature.setObjectName(u"signature")
        self.signature.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.signature, 5, 0, 1, 2)

        self.set_tr = QPushButton(self.centralwidget)
        self.set_tr.setObjectName(u"set_tr")
        icon.addPixmap(QtGui.QPixmap(tr_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set_tr.setIcon(icon)
        self.set_tr.setIconSize(QtCore.QSize(80, 40))

        self.gridLayout.addWidget(self.set_tr, 4, 1, 1, 1)

        self.genButton = QPushButton(self.centralwidget)
        self.genButton.setObjectName(u"genButton")

        self.gridLayout.addWidget(self.genButton, 3, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")
        self.info.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.info, 1, 0, 1, 2)

        self.copyButton = QPushButton(self.centralwidget)
        self.copyButton.setObjectName(u"copyButton")

        self.gridLayout.addWidget(self.copyButton, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, "en")

        QMetaObject.connectSlotsByName(MainWindow)

        self.genButton.clicked.connect(self.generating)
        self.copyButton.clicked.connect(self.copying)
        self.set_en.clicked.connect(lambda: self.retranslateUi(MainWindow, "en"))
        self.set_tr.clicked.connect(lambda: self.retranslateUi(MainWindow, "tr"))

    # setupUi

    def retranslateUi(self, MainWindow, lang):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"imPASSible", None))
        self.set_en.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.linePwd.setText(QCoreApplication.translate("MainWindow", u"Click \"Generate!\"" if lang == "en" else u"\"Oluştur!\"a tıkla" , None))
        self.signature.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Oguz Alp Cakmak - Galatasaray University - 2022</span></p></body></html>", None))
        self.set_tr.setText(QCoreApplication.translate("MainWindow", u"Türkçe", None))
        self.genButton.setText(QCoreApplication.translate("MainWindow", u"Generate!" if lang == "en" else u"Oluştur!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">imPASSible</span></p></body></html>", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Generate a strong password!</span></p></body></html>" if lang == "en" else u"<html><head/><body><p><span style=\" font-size:24pt;\">Güçlü bir şifre oluştur!</span></p></body></html>", None))
        self.copyButton.setText(QCoreApplication.translate("MainWindow", u"Copy" if lang == "en" else u"Kopyala", None))
    # retranslateUi

    def generating(self):
        self.linePwd.setText(superset(3))


    def copying(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.linePwd.displayText())

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())

main()
