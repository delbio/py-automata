from automaton.core.Action import Action


class CheckExit(Action):

    def execute(self, *arg):
        print(self.getName()+" with arg: ")
        pass
