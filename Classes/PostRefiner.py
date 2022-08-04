import nltk
import json
import os
from Classes.PathHandler import PathHandler
from Parameters.paths import paths

class PostRefiner():
    def __init__(self) -> None:
        self.pathHandler = PathHandler(paths)



    def loadRawPost(self,name):
        """
            Loads a post from Raw Post
        """
        data = open(self.pathHandler.getRawPostsPath() +name+".json")
        return json.load(data)
    
    def loadLabeledPost(self,name):
        """
            Loads a post from Raw Post
        """
        data = open(self.pathHandler.getLabeledPostsPath()+name)
        return json.load(data)

    
    def _tokenizeComment(self,comment):
        return nltk.word_tokenize(comment)

    def tokenizeLabelizedPost(self,labeledPost):

        """
            Depth first search to lemmatized the given post
        """
        tokenisedPost = {"title": labeledPost["title"],"content":[]}


        for labeledComment in labeledPost["content"]:

            tokenisedPost["content"].append({"label":labeledComment["label"] ,"comment":self._tokenizeComment(labeledComment["comment"])})
        

        
        self._dumpRefinedPostToJSON(tokenisedPost)

    def _dumpRefinedPostToJSON(self,post):
        print(post)
        """
            Internal function used to create a JSON file from Raw JSON post
        """
        name = self.pathHandler.getRefinedPostsPath()+post["title"]+""".json"""
        
        with open(name, 'w') as outfile:
            json.dump(post, outfile)


    

    def _getAllLabeledPosts(self):
        return os.listdir(self.pathHandler.getLabeledPostsPath())



    def refineAllLabelisedPosts(self):

        for post in self._getAllLabeledPosts():
            self.tokenizeLabelizedPost(self.loadLabeledPost(post))


    # Convert to bag of words 
    








            