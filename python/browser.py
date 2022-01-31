# Importing the libraries
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import * 

# Classes or functions 
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com/"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        previousButton = QAction("Previous", self)
        previousButton.triggered.connect(self.browser.back) 
        navbar.addAction(previousButton)

        nextButton = QAction("Next", self)
        nextButton.triggered.connect(self.browser.forward) 
        navbar.addAction(nextButton)

        refreshButton = QAction("Reload", self)
        refreshButton.triggered.connect(self.browser.reload) 
        navbar.addAction(refreshButton)

        homeButton = QAction("Home", self)
        homeButton.triggered.connect(self.home)
        navbar.addAction(homeButton)

        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)

        self.browser.urlChanged.connect(self.updateUrl)

    def home(self):
        self.browser.setUrl(QUrl("https://www.google.com/"))

    def loadUrl(self):
        url = "https://www." + self.searchBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, url):
        self.searchBar.setText(url.toString())

# Main function 
app = QApplication(sys.argv)
QApplication.setApplicationName("My Web Browser")
window = Window()
app.exec_()