class Persona:
    def __init__(self,Id, nombre, apellido , ident, email, password, foto, telefono):
        self.__id = Id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__identificacion = ident
        self.__correo = email
        self.__password = password
        self.__foto = foto
        self.__telefono = telefono

    def getId(self):
        return self.__id

    def setId(self,ID):
        self.__id = ID

    def __str__(self) -> str:
        return "ID: " + self.getId() + ""
