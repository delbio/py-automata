import StateInterface
import inspect

class State(StateInterface.StateInterface):
    def getName(self):
        return self.__class__.__name__
    def getNextInputs(self):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    def getNextiActions(self):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    def getAction(self, actionName):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    def addAction(self, action):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
