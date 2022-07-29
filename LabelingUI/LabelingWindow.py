import typing
import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Classes.DataLabeler import DataLabeler
from Classes.PathHandler import PathHandler
from Parameters.paths import paths

from LabelingUI.LabelPost import LabelPost


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
            #label.setFixedSize(200,200)
            #label.setStyleSheet("background-color: grey")
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
        
        text = " Title : "+ post["title"] + "\n"
        label = QLabel(text)
     

        self.labelList = [label]
        
        for comment in post["comments"]:
            self._recursiveFetch(comment,1)
        
        for label in self.labelList:
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
            
    def labelPost(self,post,label):
        """

            Function in charge of attributing a label, to be trigerred by the user inputs

        """
        post["label"] = label
        self.dataLabeler._saveLabeledPost(post)
        self.parentWidget.currentIndex+=1
        if self.parentWidget.currentIndex > len(self.parentWidget.posts):
            self.parentWidget.posts = self._loadPosts()
            self.parentWidget.currentIndex = 0

        self.parentWidget._redrawWindow()
        self.startLabelizingPost(self.parentWidget.posts[self.parentWidget.currentIndex])


    def keyPressEvent(self, e):
        """
            KeyBoard input redirection

        """

        if e.text() == "a":
            self.labelPost(self.loadedPost,1)
        elif e.text() == "z":
            self.labelPost(self.loadedPost,2)
        elif e.text() == "e":
            self.labelPost(self.loadedPost,3)
        elif e.text() == "r":
            self.labelPost(self.loadedPost,4)
        elif e.text() == "t":
            self.labelPost(self.loadedPost,5)


    def __init__(self, parent: typing.Optional['QWidget'] = ...) -> None:
        super(LabelingWindow,self).__init__(parent)
        self.pathHandler = PathHandler(paths=paths)
        self.dataLabeler = DataLabeler(self.pathHandler)
        self.oldPos = QPoint(0,0)
        self.parentWidget = parent
        print(parent)

        
        
        self.screenDim = self.screen().availableGeometry().getCoords()
        print(self.screenDim[2]-100)


        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.setGeometry(0,0,1500,1500)
        self.setMaximumSize(1500,1500)

        self.readZoneWidget = LabelPost(self)


        self.layout.addWidget(self.readZoneWidget,0,0,5,5)

        self.buttonVeryBullish = QPushButton("VeryBullish")
        self.layout.addWidget(self.buttonVeryBullish,6,0,1,1)
        self.buttonVeryBullish.clicked.connect(lambda:self.labelPost(self.parentWidget.loadedPost,1))

        self.buttonBullish = QPushButton("Bullish")
        self.layout.addWidget(self.buttonBullish,6,1,1,1)
        self.buttonBullish.clicked.connect(lambda:self.labelPost(self.parentWidget.loadedPost,2))

        self.buttonNeutral = QPushButton("Neutral")
        self.layout.addWidget(self.buttonNeutral,6,2,1,1)
        self.buttonNeutral.clicked.connect(lambda:self.labelPost(self.parentWidget.loadedPost,3))


        self.buttonBearish = QPushButton("Bearish")
        self.layout.addWidget(self.buttonBearish,6,3,1,1)
        self.buttonBearish.clicked.connect(lambda:self.labelPost(self.parentWidget.loadedPost,4))


        self.buttonVeryBearish = QPushButton("VeryBearish")
        self.layout.addWidget(self.buttonVeryBearish,6,4,1,1)
        self.buttonVeryBearish.clicked.connect(lambda:self.labelPost(self.parentWidget.loadedPost,5))

        self.parentWidget.posts = self._loadPosts()
        self.startLabelizingPost(self.parentWidget.posts[0])


