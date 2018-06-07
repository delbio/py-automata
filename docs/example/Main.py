import sys

from automaton.core.Action import Action
from automaton.core.Automaton import Automaton

sys.path.append('./actions')
import actions.CopyFile
import actions.GenerateTextFile
import actions.CheckExit
from States import CopiedFile, NotStarted, GeneratedTextFile, ExitChecked


def main_fsm():
    # create state instances
    notstarted = NotStarted()
    copiedFile = CopiedFile()
    generatedTextFile = GeneratedTextFile()
    exitChecked = ExitChecked()
    # create state/action graph
    notstarted.addAction(actions.CopyFile.CopyFile(notstarted, copiedFile))
    copiedFile.addAction(Action(copiedFile))
    copiedFile.addAction(actions.GenerateTextFile.GenerateTextFile(copiedFile, generatedTextFile))
    generatedTextFile.addAction(actions.CheckExit.CheckExit(generatedTextFile, exitChecked))

    automaton = Automaton()
    for s in [notstarted, copiedFile, generatedTextFile, exitChecked]:
        print(s)
        automaton.addState(s)
    automaton.addEnd(exitChecked)
    automaton.setBegin(notstarted)

    automaton.checkIntegrity()
    automaton.setCurrentState(notstarted)
    print(automaton)
    print(automaton.getCurrentState())
    while not automaton.isFinished():
        nextInputs = automaton.getCurrentState().getNextInputs()
        print("next inputs: " + ','.join(list(nextInputs)))
        actionName = None
        if len(nextInputs) == 1:
            actionName = nextInputs[0]
        else:
            actionName = input('user must select an action: ' + ''.join(list(nextInputs)))
        automaton.doAction(actionName)
        automaton.move(actionName)
        print(automaton.getCurrentState())


if __name__ == "__main__":
    main_fsm()
