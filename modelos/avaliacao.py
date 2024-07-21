import numpy
class Avaliacao():
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = numpy.clip(nota, 1, 5)
