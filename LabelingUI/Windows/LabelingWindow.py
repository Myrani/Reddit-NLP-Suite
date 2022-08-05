import typing
import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Classes.DataLabeler import DataLabeler
from Classes.PathHandler import PathHandler
from Parameters.paths import paths

from LabelingUI.Widgets.LabelPost import LabelPost


class LabelingWindow(QWidget):
    """
        

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

    """

    # Real soft

    def _recursiveFetch(self,comment,deepness):
        """
            Recursive parcour function to fetch all the replies of a comment. 

            Args : 
                Comment : A Dict Structure representing a comment into the Post File
                deepness : the current deepness of the comment

            return : Str : The fetched replies in an indented Str Format 
        
        """
        
        if comment["replies"]:
            
            print(comment["replies"])
            label = QLabel( "\n "+deepness*"   |"+comment["body"])
            self.labelList.append(label)
            
            for reply in comment["replies"]:
                self._recursiveFetch(reply,deepness+1)

        else:
            return None
    
    def _loadPosts(self):
        """
        
            Fetch a list of files into a U
        
        
        """
        return self.dataLabeler.loadRandomPostsFromRandomDirectory()
    
    
    def _loadPostIntoUi(self,post):

        """
            Function to load a post into the user UI , recursively parcour the post file and fetch all the comments
        """
        
        text = post["title"] + "\n"
        label = QLabel(text)
     

        self.labelList = [label]
        
        for comment in post["comments"]:
            self._recursiveFetch(comment,1)
        
        
        self.readZoneWidget.addChildList(self.labelList)

        print(self.labelList)


    def startLabelizingPost(self,postPath):
        """
        Args : 
            PostPath : STR , a File path to PostFile 

            Given a filepath to a post starts the labzelization process
        """
        print(postPath)

        self.parentWidget.loadedPost = json.load(open(postPath))
        self._loadPostIntoUi(self.parentWidget.loadedPost)
    
    def _getLabelizedContent(self):
        
        labelisedContent = []

        flag = True
        for child in self.readZoneWidget.scrollArea.children():

            if flag:
                flag = not flag 
                pass
            else:    
                labelisedContent.append({"label":child.comboBox.currentText(),"comment":child.mainLabel.text().replace("|","").replace("\n","") })

        return labelisedContent
    
    def labelPost(self,post):
        """

            Function in charge of attributing a label, to be trigerred by the user inputs

        """
        labeledPost = {"title": post["title"]}

        labeledPost["content"] = self._getLabelizedContent()
        self.dataLabeler._saveLabeledPost(labeledPost)
        self.parentWidget.currentIndex+=1
        if self.parentWidget.currentIndex > len(self.parentWidget.posts):
            self.parentWidget.posts = self._loadPosts()
            self.parentWidget.currentIndex = 0

        self.parentWidget._redrawWindow()
        


    def keyPressEvent(self, e):
        """
            KeyBoard input redirection

        """

        if e.text() == "a":
            self.labelPost(self.parentWidget.loadedPost)
        elif e.text() == "z":
            self.labelPost(self.parentWidget.loadedPost)
        elif e.text() == "e":
            self.labelPost(self.parentWidget.loadedPost)
        elif e.text() == "r":
            self.labelPost(self.parentWidget.loadedPost)
        elif e.text() == "t":
            self.labelPost(self.parentWidget.loadedPost)


    def __init__(self, parent: typing.Optional['QWidget'] = ...) -> None:
        super(LabelingWindow,self).__init__(parent)
        self.pathHandler = PathHandler(paths=paths)
        self.dataLabeler = DataLabeler(self.pathHandler)
        self.oldPos = QPoint(0,0)
        self.parentWidget = parent
        

        self.screenDim = self.screen().availableGeometry().getCoords()


        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.setGeometry(0,0,1500,1500)
        self.setMaximumSize(1500,1500)

        self.readZoneWidget = LabelPost(self)


        self.layout.addWidget(self.readZoneWidget,0,0,5,5)

        self.buttonVeryBullish = QPushButton("Last Post")
        self.layout.addWidget(self.buttonVeryBullish,6,0,1,1)
        self.buttonVeryBullish.clicked.connect(lambda:self.labelPost(self.parentWidget.loadedPost))




        self.buttonVeryBearish = QPushButton("Next Post")
        self.layout.addWidget(self.buttonVeryBearish,6,4,1,1)
        self.buttonVeryBearish.clicked.connect(lambda:self.labelPost(self.parentWidget.loadedPost))

        self.parentWidget.posts = self._loadPosts()
        self.startLabelizingPost(self.parentWidget.posts[self.parentWidget.currentIndex])


