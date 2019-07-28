from fsm.core import interfaces as _i

class Automaton(_i.AutomatonInterface):
    def __init__(self):
        self._begin = None
        self._end = []
        self._state = None
        self._states = {}

    def getName(self):
        return self.__class__.__name__

    def getBegin(self):
        return self._begin

    def setBegin(self, begin):
        if begin is None:
            raise ValueError('invalid argument, end must be passed')
        if self._begin is not None:
            raise ValueError('begin state already defined')
        if begin not in self._states.values():
            raise ValueError('begin state not declared in the automaton')
        self._begin = begin

    def addEnd(self, end):
        if end is None:
            raise ValueError('invalid argument, end must be passed')
        if end not in self._states.values():
            raise ValueError('end state not declared in the automaton')
        if end in self._end:
            raise ValueError('end state already added')
        self._end.append(end)

    def getEnd(self):
        return self._end

    def addState(self, state):
        self._states[state.getName()] = state

    def getState(self, name):
        if name is None:
            raise ValueError('invalid argument, name must be passed')
        if not isinstance(name, str):
            raise ValueError('name must be a string')
        return self._states[name]

    def getStates(self):
        return list(self._states.values())

    def getCurrentState(self):
        return self._state

    def move(self, actionName):
        if actionName is None:
            raise ValueError('invalid argument, actionName must be passed')
        if not isinstance(actionName, str):
            raise ValueError('actionName must be a string')
        s = self.getCurrentState()
        if s is None:
            raise ValueError('current state not selected in the automaton')
        a = s.getAction(actionName)
        s = a.getTargetState()
        self.setCurrentState(s)

    def doAction(self, actionName, *args, **kargs):
        if actionName is None:
            raise ValueError('invalid argument, actionName must be passed')
        if not isinstance(actionName, str):
            raise ValueError('actionName must be a string')
        s = self.getCurrentState()
        if s is None:
            raise ValueError('current state not selected in the automaton')
        a = s.getAction(actionName)
        return a.execute(*args, **kargs)

    def setCurrentState(self, state):
        if len(self._end) == 0:
            raise ValueError('incomplete automaton: end state(s) not defined')
        if self._begin is None:
            raise ValueError('incomplete automaton: begin state not defined')
        if state is None:
            raise ValueError('automaton state cannot be None')
        if state not in self._states.values():
            raise ValueError('incomplete automaton: state is not defined in the automaton')
        self._state = state

    def setCurrentStateByName(self, stateName):
        if stateName is None:
            raise ValueError('invalid argument, stateName must be passed')
        if not isinstance(stateName, str):
            raise ValueError('stateName must be a string')
        return self.setCurrentState(selg.getState(stateName))

    def isFinished(self):
        return self.getCurrentState() in self._end

    def checkIntegrity(self):
        b = self.getBegin()
        if b is None:
            raise ValueError('automaton has not initial state')
        if len(b.getNextActions()) == 0 and b in self._end:
            raise ValueError('initial state ' + b.__str__() + ' is a dead-end (has no outgoing action)')
        el = self.getEnd()
        if len(el) == 0:
            raise ValueError('automaton has no end state')
        for e in el:
            if len(e.getNextActions()) > 0 and e != b:
                raise ValueError('end state ' + e.__str__() + ' must be a dead-end (must not have outgoing actions)')
        for e in self.getStates():
            if len(e.getNextActions()) == 0 and e not in self._end:
                raise ValueError('state ' + e.__str__() + ' is dead-end (has no outgoing actions)')

    def __str__(self):
        result = self.getName() + ': state->actions mapping '
        result += '{ '
        states = list(self._states.values())
        for sidx, s in enumerate(states):
            for aidx, a in enumerate(s.getNextActions()):
                result += s.__str__() + '.' + a.__str__()
                if aidx < len(s.getNextActions()) - 1:
                    result += ', '

            if sidx < len(states) - 1:
                result += '; '
        result += ' }'
        return result
