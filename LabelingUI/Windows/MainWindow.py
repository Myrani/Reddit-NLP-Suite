from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction
from PyQt6.QtCore import  QPoint,Qt
from LabelingUI.Windows.LabelMenuWindow import LabelMenuWindow

from LabelingUI.Windows.LabelingWindow import LabelingWindow
from LabelingUI.Windows.LabelCreationWindow import LabelCreationWindow

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setWindowTitle("Data Labeling")
        self.setGeometry(100,100,400,600)
        self.setMaximumSize(1500,1500)
   
        self.menu = self.menuBar()

        self.createLabelSet = QAction('Label sets', self)
        self.createLabelSet.triggered.connect(self._redrawLabelMenuWindow)
        self.menu.addAction(self.createLabelSet)

        self.gotoLabelisationWindowAction = QAction('Go to Labelisation Window', self)
        self.gotoLabelisationWindowAction.triggered.connect(self._redrawWindow)
        self.menu.addAction(self.gotoLabelisationWindowAction)

        #file_menu.addAction(button_action)
        
        # Current active label set (Not temporary)

        self.currentActiveLabels = []

        # Label sets creation temporary stockage

        self.labelSet_Name = ""
        self.labelSet_LabelList = [] 


        # Labelisation process variables 
        self.currentIndex = 0
        
        self.initUI()

    
    ### Dragable window part
    
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.position().toPoint()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.position().toPoint() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        
    def mouseReleaseEvent(self, event):
        self.oldPos = event.position().toPoint()
    
    def initUI(self):
        #self.labelingWindow = LabelingWindow(self)
        self.labelCreationWindow = LabelMenuWindow(self)

        self.setCentralWidget(self.labelCreationWindow)
        self.show()

    def _redrawWindow(self):
        self.labelingWindow = LabelingWindow(self)
        self.setCentralWidget(self.labelingWindow)
        self.show()

    def _redrawLabelMenuWindow(self):
        self.labelSet_LabelList = [] 
        self.labelMenuWindow = LabelMenuWindow(self)
        self.setCentralWidget(self.labelMenuWindow)
        self.show()

    def _redrawLabelCreationWindow(self):
        self.labelCreationWindow = LabelCreationWindow(self)
        self.setCentralWidget(self.labelCreationWindow)
        self.show()