from turtle import title
import nltk
import json

class PostRefiner():
    def __init__(self) -> None:
        pass

    # Lemmatize Comment from post


    def loadRawPost(self,name):
        """
            Loads a post from Raw Post
        """
        data = open("RawPosts/"+name+".json")
        return json.load(data)

    def loadRefinedPost(self,name):
        """
            Loads a post from Raw Post
        """
        data = open("RefinedPosts/"+name+".json")
        return json.load(data)

    def _fetchNextReplyToLemmatize(self,comment):

        """
            Depth first search to lemmatized the given post
        """

        lemmatizedComment ={"comment":nltk.word_tokenize(comment["body"]),"replies":[]}
        
        if comment["replies"]:
            for reply in comment["replies"]:
                lemmatizedComment["replies"].append(self._fetchNextReplyToLemmatize(reply))

        return lemmatizedComment
        
    def _dumpLemmatizedPostToJSON(self,post):
        print(post)
        """
            Internal function used to create a JSON file from Raw JSON post
        """
        name = """RefinedPosts/"""+post["title"]+""".json"""
        
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





            