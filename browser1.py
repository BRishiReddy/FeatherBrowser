import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
 
class MainWindow(QMainWindow):	
	def __init__(self):
		super(MainWindow,self).__init__()

		self.tabs = QTabWidget()
		self.tabs.setDocumentMode(True)
		self.tabs.setTabsClosable(True)

		self.setCentralWidget(self.tabs)

		self.tabs.tabBarDoubleClicked.connect(self.tab_open_double_click)

		self.tabs.tabCloseRequested.connect(self.close_current_tab)

		#tool bar
		navtb = QToolBar("Navigation")
		navtb.setIconSize(QSize(20,20)) 
		self.addToolBar(navtb)

		#buttons
		bac_but=QAction('back',self)
		bac_but.setIcon(QIcon('3.png'))
		navtb.addAction(bac_but) 
		self.add_new_tab(QUrl('https://www.google.com'),'Homepage')
		self.show()





	def add_new_tab(self,qurl=None,label="blank"):
		if qurl is None:
		    qurl = QUrl("")

		browser = QWebEngineView()
		browser.setUrl(qurl)

		i = self.tabs.addTab(browser,label)
		self.tabs.setCurrentIndex(i)

	def tab_open_double_click(self,i):
		if i == -1:
			self.add_new_tab()

	def close_current_tab(self,i):
		if self.tabs.count() <2:
			return 
		self.tabs.removeTab(1)




	    

		

		




app = QApplication(sys.argv)
app.setApplicationName("Feather")

window = MainWindow()
app.exec_()

 		