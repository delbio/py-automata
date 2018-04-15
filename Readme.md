## Come implementare una interfaccia in Python

https://stackoverflow.com/a/31439126/3753724

usare Base Abstract Class

```python
import abc

class InterfaceName(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError('users must define __str__ to use this base class')
```

## Come recuperare il nome della metodo nella quale mi trovo

uso questa tecnica per non dover scrivere il nome del metodo dell'interfaccia da implementare

https://stackoverflow.com/a/5067654/3753724

## Come recuperare il nome della classe

https://stackoverflow.com/a/511060/3753724

## Comporre il file .gitignore

```
wget https://www.gitignore.io/api/python -O .gitignore
wget https://www.gitignore.io/api/vim -O ->> .gitignore
```

## Come usare le variabili all'interno di una classe

https://stackoverflow.com/a/5690920/3753724

## Python null equivalent

https://www.pythoncentral.io/python-null-equivalent-none/
