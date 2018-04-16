import sys
sys.path.append('./src')
sys.path.append('./examples')
## aggiungo al path dove cerca le classi python anche quella che
## contiene i miei sorgenti
## https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

from src.State import State
from src.Action import Action
from src.Automaton import Automaton
import examples.States
import examples.Actions

def main():
    # create state instances
    nuovo = examples.States.Nuovo()
    cancellato = examples.States.Cancellato()
    pubblicabile = examples.States.Pubblicabile()
    pubblicato = examples.States.Pubblicato()

    # create state/action graph
    nuovo.addAction(examples.Actions.Elimina(nuovo, cancellato))
    nuovo.addAction(examples.Actions.Modifica(nuovo, pubblicabile))
    pubblicabile.addAction(examples.Actions.Elimina(pubblicabile, cancellato))
    pubblicabile.addAction(examples.Actions.Pubblica(pubblicabile, pubblicato))
    pubblicabile.addAction(examples.Actions.Modifica(pubblicabile, pubblicabile))
    pubblicato.addAction(examples.Actions.Modifica(pubblicato, pubblicabile))

    automaton = Automaton()
    for s in [nuovo,cancellato,pubblicabile,pubblicato]:
        print(s)
        automaton.addState(s)
    automaton.addEnd(cancellato)
    automaton.setBegin(nuovo)

    automaton.checkIntegrity()
    automaton.setCurrentState(nuovo)
    print(automaton)
    print(automaton.getCurrentState())
    for a in ['Modifica', 'Pubblica', 'Modifica', 'Modifica', 'Elimina']:
        print(a)
        automaton.doAction(a)
        automaton.move(a)
        print(automaton.getCurrentState())

if __name__ == "__main__":
    main()
