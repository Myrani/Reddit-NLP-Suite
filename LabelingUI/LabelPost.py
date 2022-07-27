from PyQt6.QtWidgets import QScrollArea,QGroupBox,QGridLayout,QScrollBar,QHBoxLayout,QWidget
from PyQt6.QtCore import Qt 


class LabelPost(QWidget):
    def __init__(self, parent=None,):
        super(LabelPost,self).__init__(parent=parent)
        self.layout = QHBoxLayout(self)
        
        self.show()

    def addChildList(self,listOfLabels):
        for label in listOfLabels:
            self.layout.addChildWidget(label)
        
        self.show()