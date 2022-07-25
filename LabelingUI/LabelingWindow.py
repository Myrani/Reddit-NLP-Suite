import typing
import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Classes.DataLabeler import DataLabeler
from Classes.PathHandler import PathHandler
from Parameters.paths import paths
class LabelingWindow(QWidget):
    

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
            text = "\n "+deepness*"   |"+comment["body"]
            
            for reply in comment["replies"]:
                text += "\n "+self._recursiveFetch(reply,deepness+1)

            return text
        else:
            return ""
    
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
        for comment in post["comments"]:
            text += self._recursiveFetch(comment,1)
        
        self.readZoneLabel.setText(text)

    def startLabelizingPost(self,postPath):
        """
        Args : 
            PostPath : STR , a File path to PostFile 

            Given a filepath to a post starts the labzelization process
        """
        
        print(postPath)

        self.loadedPost = json.load(open(postPath))
        self._loadPostIntoUi(self.loadedPost)
            
    def labelPost(self,post,label):
        """


            Function in charge of attributing a label, to be trigerred by the user inputs

        """
        post["label"] = label
        self.dataLabeler._saveLabeledPost(post)
        self.currentIndex+=1
        if self.currentIndex > len(self.posts):
            self.posts = self._loadPosts()
            self.currentIndex = 0

        self.startLabelizingPost(self.posts[self.currentIndex])


    def keyPressEvent(self, e):
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
        self.setParent(parent)

        
        self.screenDim = self.screen().availableGeometry().getCoords()
        print(self.screenDim[2]-100)


        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.setGeometry(0,0,1500,1500)
        self.setMaximumSize(1500,1500)

        self.readZoneLabel = QLabel("Test")
        #self.readZoneLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.readZoneLabel.setStyleSheet("background-color:grey")
        self.layout.addWidget(self.readZoneLabel,0,0,1,5)


        self.buttonVeryBullish = QPushButton("VeryBullish")
        self.layout.addWidget(self.buttonVeryBullish,1,0,1,1)
        self.buttonVeryBullish.clicked.connect(lambda:self.labelPost(self.loadedPost,1))

        self.buttonBullish = QPushButton("Bullish")
        self.layout.addWidget(self.buttonBullish,1,1,1,1)
        self.buttonBullish.clicked.connect(lambda:self.labelPost(self.loadedPost,2))

        self.buttonNeutral = QPushButton("Neutral")
        self.layout.addWidget(self.buttonNeutral,1,2,1,1)
        self.buttonNeutral.clicked.connect(lambda:self.labelPost(self.loadedPost,3))


        self.buttonBearish = QPushButton("Bearish")
        self.layout.addWidget(self.buttonBearish,1,3,1,1)
        self.buttonBearish.clicked.connect(lambda:self.labelPost(self.loadedPost,4))


        self.buttonVeryBearish = QPushButton("VeryBearish")
        self.layout.addWidget(self.buttonVeryBearish,1,4,1,1)
        self.buttonVeryBearish.clicked.connect(lambda:self.labelPost(self.loadedPost,5))

        self.posts = self._loadPosts()
        self.currentIndex = 0
        self.startLabelizingPost(self.posts[0])


