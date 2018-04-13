import abc
import inspect

class ActionInterface(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getName(self):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    @abc.abstractmethod
    def execute(self, args):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    @abc.abstractmethod
    def getTargetState(self):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
    @abc.abstractmethod
    def getOriginState(self, actionName):
        raise NotImplementedError('users must define '+inspect.stack()[0][3]+' to use this base class')
