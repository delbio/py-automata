import abc
import inspect

class StateInterface(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getName(self):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    @abc.abstractmethod
    def getNextInputs(self):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    @abc.abstractmethod
    def getNextiActions(self):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    @abc.abstractmethod
    def getAction(self, actionName):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    @abc.abstractmethod
    def addAction(self, action):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')

