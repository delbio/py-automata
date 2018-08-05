import sys

from automaton.core.Action import Action
from automaton.core.Automaton import Automaton
from Builder import Builder

sys.path.append('./actions')
import actions.CopyFile
import actions.GenerateTextFile
import actions.CheckExit
from States import CopiedFile, NotStarted, GeneratedTextFile, ExitChecked

from defusedxml.ElementTree import fromstring, parse
import xml.etree.ElementTree as ET


def build_from_xml(filepath):
    builder = Builder()
    root = parse(filepath).getroot()
    automaton = builder.newObjectFromXmlElement(root)
    print('Loaded Automaton: \n', automaton.__str__())
    runner(automaton)

def runner(automaton):
    print('Start from:\t', automaton.getCurrentState())
    while not automaton.isFinished():
        nextInputs = automaton.getCurrentState().getNextInputs()
        print("\tNext inputs:\t" + ', '.join(list(nextInputs)))
        actionName = None
        if len(nextInputs) == 1:
            actionName = nextInputs[0]
        else:
            actionName = input('User must select an action: ' + ', '.join(list(nextInputs)) + ' : ')
        automaton.doAction(actionName)
        automaton.move(actionName)
        print('Current State:\t',automaton.getCurrentState())

if __name__ == "__main__":
    build_from_xml('config.xml')
