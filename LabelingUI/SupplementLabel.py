from PyQt6.QtWidgets import QLabel,QScrollArea,QGroupBox,QGridLayout,QScrollBar,QHBoxLayout,QWidget,QVBoxLayout,QFrame,QComboBox,QSizePolicy
from PyQt6.QtCore import Qt 


class SupplementLabel(QWidget):
    
    def __init__(self, parent) -> None:

        super(SupplementLabel,self).__init__(parent=parent)
        self.widgetLayout = QVBoxLayout(self)

        self.mainlabel = QLabel(self)
        self.comboBox =  QComboBox(self)
        self.mainlabel.setStyleSheet("background-color: grey")

        self.mainlabel.setMinimumSize(100,100)
        self.mainlabel.setMaximumSize(400,400)
        
        self.mainlabel.setWordWrap(True)
        self.mainlabel.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Preferred)
        self.mainlabel.adjustSize()
        
        self.comboBox.addItems(["Neutral","Very Bullish","Bullish","Bearish","Very Bearish"])
        self.comboBox.setMaximumSize(200,25)



        self.widgetLayout.addWidget(self.mainlabel)
        self.widgetLayout.addWidget(self.comboBox)
        
        
        self.show()

        
    
    def setText(self,text):
        self.mainlabel.setText(text)
        self.mainlabel.adjustSize()