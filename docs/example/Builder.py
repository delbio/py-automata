# inspired by:
# https://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported
import importlib

def getClassFromElement(element):
    return getclass(element.attrib['module'], element.attrib['name'])

def getclass(module_name, class_name):
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

# Manage State Type actions

def setBegin(a, s, t):
    a.setBegin(s)

def addEnd(a, s, t):
    a.addEnd(s)

def nop(a, s, t):
    pass

def unknownStateType(a, s, t):
    raise ValueError("state type unknown: " + t ) 
    
class Builder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        automaton = getClassFromElement(element)()

        switcher = {
            'BEGIN': setBegin,
            'END': addEnd,
            '-': nop,
        }

        stateNodes = element.findall('States/State');
        for stateElement in stateNodes:
            state = getClassFromElement(stateElement)()
            automaton.addState(state)
            stateType = stateElement.attrib['type']
            switcher.get(stateType, unknownStateType )(automaton, state, stateType)

        actionNodes = element.findall('Actions/Action')
        for actionElement in actionNodes:
            sourceState = automaton.getState(actionElement.attrib['source'])
            targetState = automaton.getState(actionElement.attrib['target'])

            action = getClassFromElement(actionElement)(sourceState, targetState)
            sourceState.addAction(action)


        automaton.setCurrentState(automaton.getBegin())
        automaton.checkIntegrity()
        print('instance', automaton.__str__())
        return automaton
