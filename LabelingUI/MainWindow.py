from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import  QPoint,Qt

from LabelingUI.LabelingWindow import LabelingWindow

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setWindowTitle("Data Labeling")
        self.setGeometry(100,100,400,600)
        self.setMaximumSize(1500,1500)
        
        
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
        self.labelingWindow = LabelingWindow(self)
   
        #self.homeWindow.move(self.screen().availableGeometry().center().x()-200,self.screen().availableGeometry().center().y()-200)

        self.setCentralWidget(self.labelingWindow)
        self.show()

    def _redrawWindow(self):
        self.labelingWindow = LabelingWindow(self)
        self.setCentralWidget(self.labelingWindow)
        self.show()