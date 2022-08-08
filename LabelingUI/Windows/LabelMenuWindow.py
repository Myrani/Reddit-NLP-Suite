import typing
from PyQt6.QtWidgets import QLabel,QScrollArea,QGroupBox,QGridLayout,QScrollBar,QHBoxLayout,QWidget,QVBoxLayout,QFrame,QComboBox,QSizePolicy
from PyQt6.QtCore import Qt 
from LabelingUI.Widgets.LabelSetCreationWidget import LabelSetCreationWidget
from LabelingUI.Widgets.LabelSetShortcutWidget import LabelSetShortcutWidget


class LabelMenuWindow(QWidget):

    def __init__(self, parent: typing.Optional['QWidget']) -> None:
        super(LabelMenuWindow,self).__init__(parent)

    
        self.setupUI()

    def setupUI(self):
        
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.placeholderWidget = LabelSetShortcutWidget("test",self)
        self.layout.addWidget(self.placeholderWidget)


        self.creationWidget = LabelSetCreationWidget(self)
        self.layout.addWidget(self.creationWidget)

        self.show()