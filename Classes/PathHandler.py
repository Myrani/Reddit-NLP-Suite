class PathHandler():

    def __init__(self,paths) -> None:
        self.path = paths

    def getRawPostsPath(self):
        return self.path["RawPostsFilePath"]
    
    def getRefinedPostsPath(self):
        return self.path["RefinedPostsFilePath"]

    def getLabeledPostsPath(self):
        return self.path["LabeledPostsFilePath"]

    def getBagOfWordsPath(self):
        return self.path["BagOfWordsFilePath"]

    def getClassifiersPath(self):
        return self.path["ClassifiersFilePath"]