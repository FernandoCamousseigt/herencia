"""
En un archivo membresia.py, crear la clase que permita definir los atributos de
instancia y comportamiento de todas las membresías. Considere:
a. Utilice abstracción para definir el o los comportamientos requeridos (puede
definir también métodos no abstractos).
b. Utilice encapsulamiento para los atributos de instancia. Declare las
propiedades que estime necesarias según lo solicitado.
"""
from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, email: str, ccard :str) -> None:
        self.__email = email
        self.__ccard = ccard

    @property
    def email(self):
        return self.__email

    @property
    def ccard(self):
        return self.__ccard

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basica(self.email, self.ccard)    
        elif nueva_membresia == 2:
            return Familiar(self.email, self.ccard)            
        elif nueva_membresia == 3:
            return SinConexion(self.email, self.ccard)          
        elif nueva_membresia == 4:
            return Pro(self.email, self.ccard)


"""
En el mismo archivo, crear la clase que permita crear instancias de membresías de
tipo Gratis. Considere:
a. Heredar la o las clases necesarias para evitar repetir implementaciones.
b. Definir los atributos de clase necesarios.
c. Definir los métodos necesarios (en caso de que se justifique).
d. Sobrescribir los métodos necesarios (en caso de que se justifique).
"""


class Gratis(Membresia):
    costo = 0
    cant_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in [1,2,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

"""
En el mismo archivo, crear la clase que permita crear instancias de membresías de
tipo Básica. Considere:
a. Heredar la o las clases necesarias para evitar repetir implementaciones.
b. Definir los atributos de clase necesarios.
c. Definir los métodos necesarios (en caso de que se justifique).
d. Sobrescribir los métodos necesarios (en caso de que se justifique).
"""

class Basica(Membresia):
    costo = 3000
    cant_dispositivos = 2

    def __init__(self, email: str, ccard :str) -> None:
        super().__init__(email, ccard)

        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7
        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in [2,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
    
    def cancelar_suscripcion(self):
        return Gratis(self.email, self.ccard)


class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in [1,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
    
    def modificar_control_parental(self) -> None:
        pass
    

