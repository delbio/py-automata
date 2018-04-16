import sys
sys.path.append('../src')
## aggiungo al path dove cerca le classi python anche quella che
## contiene i miei sorgenti
## https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

from src.Action import Action

class Elimina(Action):
    pass
class Modifica(Action):
    pass
class Pubblica(Action):
    pass
