import abc
import inspect as _inspect

class ActionInterface(object, metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def getName(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def execute(self, *args):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getTargetState(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getOriginState(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

class StateInterface(object, metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def getName(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getNextInputs(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getNextActions(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getAction(self, actionName):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def addAction(self, action):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')


class AutomatonInterface(object, metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def getName(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getBegin(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getEnd(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getState(self, name):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getStates(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def getCurrentState(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def move(self, actionName):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def doAction(self, actionName, *parms):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def setCurrentState(self, state):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def setCurrentStateByName(self, stateName):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def isFinished(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')

  @abc.abstractmethod
  def checkIntegrity(self):
    raise NotImplementedError('users must define ' + _inspect.stack()[0][3] + ' to use this base class')
