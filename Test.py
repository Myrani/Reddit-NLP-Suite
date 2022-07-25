import time
import praw

from psaw import PushshiftAPI
import datetime as dt



reddit = praw.Reddit(
            client_id="dDbg_hJrm0bHaXOxvI1etw",
            client_secret="tFgAvfmPbfUbx8EB3lWomu_1J6Qb2A",
            user_agent="Accel",
        )


api = PushshiftAPI(reddit)

start_epoch=int(dt.datetime(2017, 1, 1).timestamp())
end_epoch=int(dt.datetime(2017, 1, 2).timestamp())

list = list(api.search_submissions(after=start_epoch,
                            before=end_epoch,
                            subreddit='CryptoCurrency',
                            score = ">10",
                            limit=10))

for el in list:
    submission = reddit.submission(el)
    print(submission.title)