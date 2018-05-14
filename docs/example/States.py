import sys

from automaton.core.State import State

class NotStarted(State):
    pass
class CopiedFile(State):
    pass
class GeneratedTextFile(State):
    pass
class ExitChecked(State):
    pass
