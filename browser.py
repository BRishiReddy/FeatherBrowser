import sys
import os
from PyQt5 import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
     def __init__(self):
         super(MainWindow,self).__init__()
         self.setWindowTitle('Feather Browser')
         self.setWindowIcon(QtGui.QIcon('feather.png'))
         self.tabs = QTabWidget()
         self.tabs.setDocumentMode(True)
         self.tabs.setTabsClosable(True)
         self.tabs.show
         self.add_new_tab(QUrl('https://www.google.com'),'Homepage')
         self.setCentralWidget(self.tabs)

         self.showMaximized()

         #tool bar 1
         nav = QToolBar()
         self.addToolBar(nav)
         nav.setMovable(False)

         #tool bar 2
         nav1 = QToolBar()
         self.addToolBar(Qt.LeftToolBarArea,nav1)

         #Menu Bar
         menuBar = self.menuBar()
        
         fileMenu = QMenu("&File", self)
         menuBar.addMenu(fileMenu)
         # Using a title
         editMenu = menuBar.addMenu("&Edit")
         # Using an icon and a title
         helpMenu = menuBar.addMenu("&Help")

         
         


         #back button
         back_but = QAction("Back",self)
         back_but.setIcon(QtGui.QIcon('3.png'))
         back_but.triggered.connect(self.back)
         nav.addAction(back_but) 

         #forward button
         for_but = QAction("forward",self)
         for_but.setIcon(QtGui.QIcon('4.png'))
         for_but.triggered.connect(self.forward)
         nav.addAction(for_but)

         #reload button
         rel_but =QAction("Reload",self)
         rel_but.setIcon(QtGui.QIcon('2.png'))
         rel_but.triggered.connect(self.reload)
         nav.addAction(rel_but)

         #home_button
         home_but=QAction("Home",self)
         home_but.setIcon(QtGui.QIcon('home.png'))
         home_but.triggered.connect(self.home)
         nav.addAction(home_but)

         #new tab
         self.tabs.tabBarDoubleClicked.connect(self.new_tab)


         #close tab
         self.tabs.tabCloseRequested.connect(self.close_current_tab)

         #tab changed
         self.tabs.currentChanged.connect(self.tab_changed)
     
         #url bar
         self.url_bar = QLineEdit()
         self.url_bar.returnPressed.connect(self.get_url)
         nav.addWidget(self.url_bar)

         #youtube
         you_but = QAction("youtube",self)
         you_but.setIcon(QtGui.QIcon('you.png'))
         you_but.triggered.connect(self.youtube) 
         nav1.addAction(you_but)

         #facebook
         fac_but=QAction("facebook",self)
         fac_but.setIcon(QtGui.QIcon('fac.png'))
         fac_but.triggered.connect(self.facebook)
         nav1.addAction(fac_but)

         #Instagram 
         insta_but=QAction('Instagram',self)
         insta_but.setIcon(QtGui.QIcon('insta.png'))
         insta_but.triggered.connect(self.intagram)
         nav1.addAction(insta_but)

         #twiter
         twi_but = QAction("twiter",self)
         twi_but.setIcon(QtGui.QIcon('twi.png'))
         twi_but.triggered.connect(self.twiter)
         nav1.addAction(twi_but)

         #NDTV
         ndtv_but = QAction("NDTV",self)
         ndtv_but.setIcon(QtGui.QIcon('nd.png'))
         ndtv_but.triggered.connect(self.ndtv)
         nav1.addAction(ndtv_but)

         #Amazon
         Am_but = QAction("Amazon",self)
         Am_but.setIcon(QtGui.QIcon('ama.png'))
         Am_but.triggered.connect(self.Amazon)
         nav1.addAction(Am_but)

         #Flipkart
         fl_but = QAction("Flipkart",self)
         fl_but.setIcon(QtGui.QIcon('flip.png'))
         fl_but.triggered.connect(self.Flipkart)
         nav1.addAction(fl_but)

         #Github
         gt_but = QAction("Github",self)
         gt_but.setIcon(QtGui.QIcon('git.png'))
         gt_but.triggered.connect(self.Github)
         nav1.addAction(gt_but)
         

         
     def home(self):
         self.tabs.currentWidget().setUrl(QUrl("https://www.google.com"))
         self.tabs.currentWidget().page().title()

         pass
     def back(self):
         self.tabs.currentWidget().back()
     def forward(self):
         self.tabs.currentWidget().forward()
     def reload(self):
         self.tabs.currentWidget().reload()


     def update_url(self,url):
         self.url_bar.setText(url.toString()) 

     def get_url(self):
         url = self.url_bar.text()
         self.tabs.currentWidget().setUrl(QUrl(url))
     
     def youtube(self):
         self.add_new_tab(QUrl('https://www.youtube.com'),'youtube')
         pass

     def facebook(self):
         self.add_new_tab(QUrl('https://www.facebook.com'),'facebook')
         pass
     def intagram(self):
         self.add_new_tab(QUrl('https://www.instagram.com'),'Instagram')
         pass

     def twiter(self):
         self.add_new_tab(QUrl('https://www.twitter.com'),'twitter')
         pass

     def ndtv(self):
         self.add_new_tab(QUrl('https://www.ndtv.com'),'NDTV')
         pass

     def Amazon(self):
         self.add_new_tab(QUrl('https://www.amazon.in'),'Amazon')
         pass

     def Flipkart(self):
         self.add_new_tab(QUrl('https://www.flipkart.com'),'Flipkart')
         pass

     def Github(self):
         self.add_new_tab(QUrl('https://github.com'),'Flipkart')
         pass


     

     def add_new_tab(self,qurl=None,label="Webpage"):
         if qurl is None:
             qurl = QUrl("https://www.google.com")


         self.browser = QWebEngineView()
         self.browser.setUrl(qurl)  

         i = self.tabs.addTab(self.browser,label)
         self.tabs.setCurrentIndex(i)
         self.browser.urlChanged.connect(self.update_url)

     def new_tab(self,i):
         if i == -1:
             self.add_new_tab()

     def close_current_tab(self,i):
         if self.tabs.count() <2:
             return 
         self.tabs.removeTab(i)

     def update_urlbar(self,q,browser=None):
         self.url_bar.setText(q.toString())
         


     def tab_changed(self,i):
         qurl=self.tabs.currentWidget().url()
         self.update_urlbar(qurl, self.tabs.currentWidget())
         self.update_title(self.tabs.currentWidget())


     def update_title(self,browser):
         if browser != self.tabs.currentWidget():
            return
         title = self.tabs.currentWidget().page().title()
         self.setWindowTitle("%s - Feather Browser"%title)
         pass






app = QApplication(sys.argv)

QApplication.setApplicationName('Feather Browser')

window = MainWindow()
app.exec_()

