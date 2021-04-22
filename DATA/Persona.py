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
        
    def getFoto(self):
        return self.__foto
    def setFoto(self, foto):
        self.__foto = foto

    def __str__(self):
        return (super().__str__() + "Nombre: " + self.getNombre() + "\n"
                + "Apellido: " + self.getApellido() + "\n"
                + "Clave de acceso: " + self.getClave() + "\n" + "Correo: "
                + self.getCorreo() + "\n" + "Identificacion: "
                + self.getIdentificacion() + "\n" + "Id Usuario: "
                + self.getID() + "\n" + "Telefono: " + self.getTelefono())
