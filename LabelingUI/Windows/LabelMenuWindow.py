import typing
from PyQt6.QtWidgets import QLabel,QScrollArea,QGroupBox,QGridLayout,QScrollBar,QHBoxLayout,QWidget,QVBoxLayout,QFrame,QComboBox,QSizePolicy
from PyQt6.QtCore import Qt
from Classes.NLP.PathHandler import PathHandler 
from LabelingUI.Widgets.LabelSetCreationWidget import LabelSetCreationWidget
from LabelingUI.Widgets.LabelSetShortcutWidget import LabelSetShortcutWidget
import os
import json 
from Parameters.paths import paths


class LabelMenuWindow(QWidget):

    def __init__(self, parent: typing.Optional['QWidget']) -> None:
        super(LabelMenuWindow,self).__init__(parent)
        self.pathHandler = PathHandler(paths=paths)
        self.setupUI()

    def _loadAllAvailableSets(self):
        return os.listdir(self.pathHandler.getLabelSetsPath())

    def _loadSet(self,setFile):
        data = open(self.pathHandler.getLabelSetsPath()+setFile)
        return json.load(data)
    def setupUI(self):
        
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        for set in self._loadAllAvailableSets():
            loadedSet = self._loadSet(set)
            widget = LabelSetShortcutWidget(loadedSet["setName"],loadedSet["labelList"],self)
            self.layout.addWidget(widget)


        self.creationWidget = LabelSetCreationWidget(self)
        self.layout.addWidget(self.creationWidget)

        self.show()