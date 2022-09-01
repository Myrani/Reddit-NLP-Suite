from typing import overload
from LabelingUI.FetchStrategies.Strategy import Strategy
from Classes.NLP.PathHandler import PathHandler
from Parameters.paths import paths
import json
import os
import datetime as dt
import random


class StrategyRandomDay(Strategy):
    def __init__(self) -> None:
        super().__init__()
        self.pathHandler = PathHandler(paths=paths)
        self._refillBuffer()


    def _selectRandomMonth(self):
        """
            Select a Random month from the RawPosts Directory .
        """

        allMonths =[month for month in os.listdir(self.pathHandler.getRawPostsPath())]
        return allMonths[random.randint(0, len(allMonths)-1)]

    def _selectRandomDay(self):
        """
            Select a Random day from the random month selected .
        
        """

        month = self._selectRandomMonth()
        allDays =[day for day in os.listdir(self.pathHandler.getRawPostsPath()+"/"+month)]

        return (month,allDays[random.randint(0, len(allDays)-1)])

    def getNextPost(self):

        with open(self.currentBuffer.pop(0)) as filename:
            element = json.load(filename)

            if not self.currentBuffer:
                self._refillBuffer()
        
            return element
            
    def _refillBuffer(self):

        tupleMonthDay = self._selectRandomDay()
        rootPath = self.pathHandler.getRawPostsPath()

        self.currentBuffer = [rootPath+"/"+tupleMonthDay[0]+"/"+tupleMonthDay[1]+"/"+file for file in os.listdir(rootPath+"/"+tupleMonthDay[0]+"/" +tupleMonthDay[1])]