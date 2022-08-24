from PyQt6.QtWidgets import QScrollArea,QGroupBox,QGridLayout,QScrollBar,QHBoxLayout,QWidget,QVBoxLayout,QFrame
from PyQt6.QtCore import Qt 
from LabelingUI.Widgets.SupplementLabel import SupplementLabel

class LabelPost(QScrollArea):
    def __init__(self, parent=None,):
        super(LabelPost,self).__init__(parent=parent)
        #self.labelPostLayout = QGridLayout(self)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)

        self.scrollArea = QFrame(self)
        self.scrollAreaLayout = QVBoxLayout(self.scrollArea)

        self.setWidget(self.scrollArea)

        self.setStyleSheet("background-color: white")
        self.show()

    def _flushPostCache(self):
        print()
        for widget in self.scrollArea.children()[1:]: 
            self.scrollAreaLayout.removeWidget(widget)



    def addWidget(self,widget):
        self.scrollAreaLayout.addWidget(widget)

    def addChildList(self,listOfLabels):
        x=0
        for label in listOfLabels:

            supplementLabel = SupplementLabel(self)
            supplementLabel.setText(label.text())
            self.addWidget(supplementLabel)
            x+=1
        self.show()
    
    def addChildListPostHistory(self,listOfLabeledComments):
        
        self._flushPostCache()
        x=0
        for post in listOfLabeledComments:

            supplementLabel = SupplementLabel(self)
            supplementLabel.setText(post["comment"])
            supplementLabel.setComboBox(post["label"])
            self.addWidget(supplementLabel)
            x+=1
        self.show()