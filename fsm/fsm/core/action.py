from fsm.core import interfaces as _i

class Action(_i.ActionInterface):
    def __init__(self, originState, targetState=None):
        self._originState = originState
        if targetState is None:
            self._targetState = originState
        else:
            self._targetState = targetState
        if originState is None:
            raise ValueError(self.__class__.__name__ + ' must have originState set')

    def getName(self):
        return self.__class__.__name__

    def execute(self, *args):
        return None

    def getTargetState(self):
        return self._targetState

    def getOriginState(self):
        return self._originState

    def __str__(self):
        return self.getName() + '() -> ' + self.getTargetState().__str__()
