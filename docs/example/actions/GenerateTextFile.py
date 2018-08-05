from automaton.core.Action import Action


class GenerateTextFile(Action):
    def execute(self, *arg):
        print(self.getName()+" with arg: ")
        pass
