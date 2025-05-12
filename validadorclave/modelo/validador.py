from abc import ABC, abstractmethod

class ValidacionError(Exception):
    pass

class LongitudInvalidaError(ValidacionError):
    pass

class MayusculaInvalidaError(ValidacionError):
    pass

class MinusculaInvalidaError(ValidacionError):
    pass

class NumeroInvalidoError(ValidacionError):
    pass

class CaracterEspecialInvalidoError(ValidacionError):
    pass

class CalistoInvalidoError(ValidacionError):
    pass

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise LongitudInvalidaError()

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise MayusculaInvalidaError()

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise MinusculaInvalidaError()

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise NumeroInvalidoError()

    @abstractmethod
    def es_valida(self, clave):
        pass
