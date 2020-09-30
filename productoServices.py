from repositorios import Repositorios


class ProductoServices:

    # Devuelve repositorio ProductoList
    def get_productosList(self):
        return Repositorios.productosList

    # Agrega producto en repositorio productosList
    # parametros : Object book
    # return: Key id
    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        id_new = int(lastKey) + 1
        Repositorios.productosList[id_new] = producto.__dict__
        return id_new

    # Eliminar producto de productosList
    # parametros: key legajo, Object producto
    def delete_producto(self, id):
        if id not in Repositorios.productosList:
            raise ValueError("El producto a elminar no existe")
        del Repositorios.productosList[id]

    # Actualiza producto en repositorio productosList
    # parametros :  key id , Object producto
    def update_producto(self, id, producto):
        if id not in Repositorios.productosList:
            raise ValueError("El id no existe")
        Repositorios.productosList.update({id: producto.__dict__})

    def delete_producto_value_error(self, id_book, legajo):
        if id not in Repositorios.productosList:
            raise ValueError("El id  existe")
