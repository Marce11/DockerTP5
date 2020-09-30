class Producto:

    def __init__(self, descripcion=' ', precio=0, tipo=' '):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo

    # getting
    @property
    def descripcion(self):
        return self._descripcion

    # setting
    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    # deleting
    @descripcion.deleter
    def descripcion(self):
        del self._descripcion

    # getting
    @property
    def precio(self):
        return self._precio

    # setting
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # deleting
    @precio.deleter
    def precio(self):
        del self._precio

    # getting
    @property
    def tipo(self):
        return self._tipo

    # setting
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    # deleting
    @tipo.deleter
    def tipo(self):
        del self._tipo
