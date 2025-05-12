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

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave):
        if not any(c in {'@', '_', '#', '$', '%'} for c in clave):
            raise CaracterEspecialInvalidoError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave):
        lower_clave = clave.lower()
        if 'calisto' not in lower_clave:
            raise CalistoInvalidoError("La clave debe contener la palabra 'calisto'")

        indices = [i for i in range(len(clave)) if lower_clave.startswith('calisto', i)]
        if not indices:
            raise CalistoInvalidoError("La clave debe contener la palabra 'calisto'")

        for idx in indices:
            substring = clave[idx:idx + 7]
            mayusculas = sum(1 for c in substring if c.isupper())
            if mayusculas < 2:
                raise CalistoInvalidoError("Debe tener al menos 2 mayúsculas en 'calisto'")
            if substring.isupper():
                raise CalistoInvalidoError("No todas las letras de 'calisto' deben ser mayúsculas")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True
