# inspired by:
# https://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported
import importlib

def getClassFromElement(element):
    return getclass(element.attrib['module'], element.attrib['name'])

def getclass(module_name, class_name):
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

class Builder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        automaton = getClassFromElement(element)()

        stateNodes = element.findall('States/State');
        for stateElement in stateNodes:
            state = getClassFromElement(stateElement)()
            automaton.addState(state)
            switcher = {
                    'BEGIN': automaton.setBegin(state),
                    'END': automaton.addEnd(state),
                    '-': None,
            }
            stateType = stateElement.attrib['type']
            if stateType not in switcher:
                raise ValueError("state type unknown: " + stateType ) 
            switcher.get(stateType, 'not founded' )

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
