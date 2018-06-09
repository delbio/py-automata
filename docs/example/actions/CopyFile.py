from automaton.core.Action import Action


class CopyFile(Action):
    def __init__(self, originState, targetState=None):
        self.filepath = None
        super(CopyFile, self).__init__(originState, targetState)
        pass

    def execute(self, *arg):
        print(self.getName()+" "+self.filepath+" with arg: ")
        pass
