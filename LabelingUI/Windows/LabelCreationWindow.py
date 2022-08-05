import typing
from PyQt6.QtWidgets import QLabel,QScrollArea,QGroupBox,QGridLayout,QScrollBar,QHBoxLayout,QWidget,QVBoxLayout,QFrame,QComboBox,QSizePolicy
from PyQt6.QtCore import Qt 
from LabelingUI.Widgets.LabelSetCreationWidget import LabelSetCreationWidget


class LabelCreationWindow(QWidget):

    def __init__(self, parent: typing.Optional['QWidget']) -> None:
        super(LabelCreationWindow,self).__init__(parent)

    
        self.setupUI()

    def setupUI(self):
        
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        
        self.creationWidget = LabelSetCreationWidget(self)
        self.layout.addWidget(self.creationWidget)

        self.show()
