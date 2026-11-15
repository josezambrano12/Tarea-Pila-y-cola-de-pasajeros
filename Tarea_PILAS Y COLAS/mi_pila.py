from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]
    ⛔ Prohibido: append, pop, insert, remove, index, sort, reverse, copy, len(), in, slicing y comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ El pasajero #{pasajero.numero} ya existe.")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desapilar(self):
        if self.cantidad == 0:
            return None
        self.cantidad = self.cantidad - 1
        elemento = self.datos[self.cantidad]
        self.datos[self.cantidad] = None
        return elemento

    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        aux = MiPila(self.capacidad)
        encontrado = False

        while self.cantidad > 0:
            actual = self.desapilar()
            if actual.numero == numero and not encontrado:
                encontrado = True
                break
            aux.apilar(actual)

        while aux.cantidad > 0:
            self.apilar(aux.desapilar())

        return encontrado

    def copiar(self):
        nueva_pila = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva_pila.apilar(self.datos[i])
        return nueva_pila

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0