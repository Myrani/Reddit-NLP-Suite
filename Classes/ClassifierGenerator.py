from Classes.PathHandler import PathHandler
from Parameters.paths import paths
import os
import json

class ClassifierGenerator():
    
    def __init__(self) -> None:
        self.pathHandler = PathHandler(paths)

    def _getAllBagOfWords(self):
        """
            Internal function used to get all bags of words in the BagOfWords Folder 
        
        """
        return os.listdir(self.pathHandler.getBagOfWordsPath())

    def _getAllClassifiers(self):
        """
            Internal function used to get all bags of words in the BagOfWords Folder 
        
        """
        return os.listdir(self.pathHandler.getClassifiersPath())

    def _loadRefinedBag(self,name):

        """
            Internal function used to load the data from a specified bag of words
        
        """
        data = open(self.pathHandler.getBagOfWordsPath()+name)
        return json.load(data)
    

    def _dumpClassiferToJSON(self,classifier):
                
        """
            Internal function used to create a JSON file from Raw JSON post
        """
        name = self.pathHandler.getClassifiersPath()+classifier["title"]+""".json"""
        
        with open(name, 'w') as outfile:
            json.dump(classifier, outfile)


    def generateClassifierFromAllBags(self):
        classifier = {}

        for bag in self._getAllBagOfWords():
            for key,value in self._loadRefinedBag(bag).items():
                if key != "title":
                    if key not in classifier:
                        classifier[key] = {}
                    for word,count in value.items():
                        if word not in classifier[key]:
                            classifier[key][word] = count
                        else:
                            classifier[key][word] = classifier[key][word] + count
        
        classifier["title"] = "Classifier_"+str(len(self._getAllClassifiers()))

        self._dumpClassiferToJSON(classifier)