import sys
sys.path.append('../src')
## aggiungo al path dove cerca le classi python anche quella che
## contiene i miei sorgenti
## https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

from src.State import State

class Nuovo(State):
    pass
class Cancellato(State):
    pass
class Pubblicabile(State):
    pass
class Pubblicato(State):
    pass
