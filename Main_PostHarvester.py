from Parameters.Secrets import secrets
from Classes.Harvesting.Harvester import Harvester

import praw


reddit = praw.Reddit(
            client_id = secrets.get("client_id"),
            client_secret = secrets.get("client_secret"),
            user_agent="Accel",
        )


harvester = Harvester(reddit)


harvester.harvestSubredditFrom("CryptoCurrency",{"day":1,"month":1,"year":2017},10)