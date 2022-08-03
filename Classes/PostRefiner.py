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


    def loadRefinedPost(self,name):
        """
            Loads a post from Raw Post
        """
        data = open(self.loadRefinedPost() +name+".json")
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

    def _dumpBagOfWordsToJSON(self,post):
        print(post)
        """
            Internal function used to create a JSON file from Raw JSON post
        """
        name = """BagOfWords/"""+post["title"]+""".json"""
        
        with open(name, 'w') as outfile:
            json.dump(post, outfile)
    

    def _getAllLabeledPosts(self):
        return os.listdir(self.pathHandler.getLabeledPostsPath())

    def refineAllLabelisedPosts(self):

        for post in self._getAllLabeledPosts():
            self.tokenizeLabelizedPost(self.loadLabeledPost(post))

    def lemmatizePost(self,post):
        """
            Master function to lematize a raw post
        """

        lemmatizedPost = {"title":post["title"],"comments":[]}

        for comment in post["comments"]:

            lemmatizedComment ={"comment":nltk.word_tokenize(comment["body"]),"replies":[]}
            
            lemmatizedComment["replies"].append(self._fetchNextReplyToLemmatize(comment))
            
            lemmatizedPost["comments"].append(lemmatizedComment)

        self._dumpLemmatizedPostToJSON(lemmatizedPost)
    
        
    # Convert to bag of words 
    
    def _fetchNextRepliesToBag(self,bag,reply):
        
        for word in reply["comment"]:
            if word in bag:
                bag[word] = bag[word]+1
            else:
                bag[word] = 1

        for reply in reply["replies"]:
            bag = self._fetchNextRepliesToBag(bag,reply)

        return bag

    def convertPostToBagOfWords(self,refinedPost):
        

        bagOfWords = {}
        
        for comment in refinedPost["comments"]:

            for word in comment["comment"]:
                if word in bagOfWords:
                    bagOfWords[word] = bagOfWords[word]+1
                else:
                    bagOfWords[word] = 1

            for reply in comment["replies"]:
                bagOfWords = self._fetchNextRepliesToBag(bagOfWords,reply)
        baggedPost = {"title":refinedPost["title"],"bag":bagOfWords}


        self._dumpBagOfWordsToJSON(baggedPost)





            