from fsm.core import interfaces as _i

class State(_i.StateInterface):
    def __init__(self):
        self._actionMap = {}

    def getName(self):
        return self.__class__.__name__

    def getNextInputs(self):
        return list(self._actionMap.keys())

    def getNextActions(self):
        return list(self._actionMap.values())

    def getAction(self, actionName):
        if actionName not in self._actionMap:
            raise ValueError('Invalid action ' + actionName + ' in state ' + self.__str__())
        else:
            return self._actionMap[actionName]

    def addAction(self, action):
        if action.getOriginState() != self:
            raise ValueError("L'origine dell'azione deve essere questo stato")
        if action.getName() in self._actionMap:
            raise ValueError(
                "cannot add action " + action.getName() + " to " + self.__str__() + ": state already has an action with the same name")
        self._actionMap[action.getName()] = action

    def __str__(self):
        return self.getName() + '[class=' + self.__class__.__name__ + ']'
