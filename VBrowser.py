from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView
import sys


class Browser(QWebView):
    def __init__(self):
        self.view = QWebView.__init__(self)
        self.setWindowTitle('VBROWSER')
        self.titleChanged.connect(self.adjustTitle)
        self.setFixedSize(300, 400)

    def load(self,url):
        self.setUrl(QUrl(url))
    
    def adjustTitle(self):
        self.setWindowTitle(self.title())
    


class Ui_VBrowser(object):
    def setupUi(self, VBrowser):
        VBrowser.setObjectName("VBrowser")
        VBrowser.resize(300, 400)
        VBrowser.setFixedSize(300, 400)
        font = QtGui.QFont()
        font.setPointSize(18)
        VBrowser.setFont(font)
        self.centralwidget = QtWidgets.QWidget(VBrowser)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(54, 260, 191, 51))
        self.pushButton.setObjectName("pushButton")
        VBrowser.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VBrowser)
        self.statusbar.setObjectName("statusbar")
        VBrowser.setStatusBar(self.statusbar)

        self.retranslateUi(VBrowser)
        QtCore.QMetaObject.connectSlotsByName(VBrowser)
        
        self.pushButton.clicked.connect(self.search)

    def retranslateUi(self, VBrowser):
        _translate = QtCore.QCoreApplication.translate
        VBrowser.setWindowTitle(_translate("VBrowser", "VBrowser"))
        self.label.setText(_translate("VBrowser", "Enter URL"))
        self.lineEdit.setPlaceholderText(_translate("VBrowser", "https://www.google.com"))
        self.pushButton.setText(_translate("VBrowser", "Search"))

    def search(self):
        text = self.lineEdit.text()
        
        if any(x in text for x in ['https://','HTTPS://','http://','HTTP://']) :
            self.view = Browser()
            self.view.show()
            self.view.load(text)
            
        elif text:
            self.view = Browser()
            self.view.show()
            self.view.load("https://www.google.com/search?q="+text)
            
        else:
            self.view = Browser()
            self.view.show()
            self.view.load("https://www.google.com")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    VBrowser = QtWidgets.QMainWindow()
    ui = Ui_VBrowser()
    ui.setupUi(VBrowser)
    VBrowser.show()
    sys.exit(app.exec_())
