from Parameters.paths import paths
from Classes.PathHandler import PathHandler
import json
import os 

class PostBagger():
    def __init__(self) -> None:
        self.pathHandler = PathHandler(paths)

    def _dumpBagOfWordsToJSON(self,bag):
        print("maye",bag)
        """
            Internal function used to create a JSON file from Raw JSON post
        """
        name = self.pathHandler.getBagOfWordsPath()+bag["title"]+""".json"""
        
        with open(name, 'w') as outfile:
            json.dump(bag, outfile)

    def _getAllRefinedPosts(self):
        return os.listdir(self.pathHandler.getRefinedPostsPath())

    def _loadRefinedPost(self,name):
        """
            Loads a post from Raw Post
        """
        data = open(self.pathHandler.getRefinedPostsPath()+name)
        return json.load(data)


    def bagAllRefinedPosts(self):
        print("pog 41")
        for post in self._getAllRefinedPosts():
            bag = self.bagRefinedPost(self._loadRefinedPost(post))
            print("pog")
            self._dumpBagOfWordsToJSON(bag)
  
    
    def _extractCommentContent(self,comment):
        

        minibag = {}

        for word in comment:
            if word in minibag:
                minibag[word] = minibag[word]+ 1
            else:
                minibag[word] = 1

        return minibag

    def bagRefinedPost(self,refinedPost):

        """
            Depth first search to lemmatized the given post
        """
        bag = {"title": refinedPost["title"]}

        for labeledComment in refinedPost["content"]:

            for key,value in self._extractCommentContent(labeledComment["comment"]).items():
                
                if labeledComment["label"] in bag:
                
                    if key in bag[labeledComment["label"]]:
                         bag[labeledComment["label"]][key] = bag[labeledComment["label"]][key] + value
                    else:
                        bag[labeledComment["label"]][key] = value        
                else:
                    bag[labeledComment["label"]] = {key:value}
        return bag