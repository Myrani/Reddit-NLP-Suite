from Parameters.Secrets import secrets
from Classes.Harvester import Harvester
from Classes.PostRefiner import PostRefiner
import praw


reddit = praw.Reddit(
            client_id = secrets.get("client_id"),
            client_secret = secrets.get("client_secret"),
            user_agent="Accel",
        )


harvester = Harvester(reddit)
postRefiner = PostRefiner()

harvester.harvestSubredditFrom("CryptoCurrency",{"day":1,"month":1,"year":2017},10)

#postRefiner.lemmatizePost(postRefiner.loadRawPost("YouTube crypto influencers are 21st century snake oil salesmen"))

#postRefiner.convertPostToBagOfWords(postRefiner.loadRefinedPost("YouTube crypto influencers are 21st century snake oil salesmen"))