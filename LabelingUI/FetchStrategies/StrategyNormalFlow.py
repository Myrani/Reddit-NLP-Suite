from typing import overload
from LabelingUI.FetchStrategies.Strategy import Strategy
from Classes.NLP.PathHandler import PathHandler
from Parameters.paths import paths
import json
import os
import datetime as dt
import random


class StrategyNormalFlow(Strategy):
    def __init__(self) -> None:
        super().__init__()
        self.pathHandler = PathHandler(paths=paths)


    @overload
    def getNextPost(self):
        """
            Select a Random day from the random month selected .
        
        """

        month = self._selectRandomMonth()
        allDays =[day for day in os.listdir(self.pathHandler.getRawPostsPath()+"/"+month)]

        return (month,allDays[random.randint(0, len(allDays)-1)])