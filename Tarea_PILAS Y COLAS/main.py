from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en orden de llegada (Diana primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  ✓ Apilado: ahora es el tope")
        elif op == "2":
            pila.listar()
        elif op == "3":
            if pila.esta_vacia():
                print("  (la pila está vacía, no se puede desapilar)")
            else:
                salio = pila.desapilar()
                print(f"  ✓ Salió: {salio.nombre} (#{salio.numero})")
                nuevo_tope = pila.ver_tope()
                if nuevo_tope:
                    print(f"  Nuevo tope: {nuevo_tope.nombre} (#{nuevo_tope.numero})")
                else:
                    print("  La pila ha quedado vacía.")
        elif op == "4":
            tope = pila.ver_tope()
            if tope:
                print(f"  Tope: {tope.nombre} ({tope.numero})")
            else:
                print("  (la pila está vacía)")
        elif op == "5":
            num = leer_entero("  Número a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                print(f"  Encontrado en [{pos}]: {pila.datos[pos].nombre}")
            else:
                print("  No existe")
        elif op == "6":
            num = leer_entero("  Número de pasajero a modificar: ")
            if pila.buscar(num) != -1:
                n_destino = input("  Nuevo destino: ").strip()
                n_asiento = input("  Nuevo asiento: ").strip().upper()
                if pila.modificar(num, n_destino, n_asiento):
                    print("  ✓ Modificado correctamente")
            else:
                print("  No existe")
        elif op == "7":
            num = leer_entero("  Número de pasajero a eliminar: ")
            if pila.eliminar_por_numero(num):
                print(f"  ✓ Pasajero #{num} eliminado")
            else:
                print("  No existe")
        elif op == "8":
            copia = pila.copiar()
            print("  ✓ Copia creada:")
            copia.listar()
        elif op == "9":
            estado = "está vacía" if pila.esta_vacia() else "no está vacía"
            print(f"  Longitud: {pila.longitud()} · {estado}")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if pila.apilar(p):
                    cargados += 1
            print(f"  ✓ {cargados} datos de prueba apilados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  ✓ Encolado: está al final")
        elif op == "2":
            cola.listar()
        elif op == "3":
            if cola.esta_vacia():
                print("  (la cola está vacía, no se puede desencolar)")
            else:
                salio = cola.desencolar()
                print(f"  ✓ Salió: {salio.nombre} (#{salio.numero})")
                nuevo_frente = cola.ver_frente()
                if nuevo_frente:
                    print(f"  Nuevo frente: {nuevo_frente.nombre} (#{nuevo_frente.numero})")
                else:
                    print("  La cola ha quedado vacía.")
        elif op == "4":
            frente = cola.ver_frente()
            if frente:
                print(f"  Frente: {frente.nombre} ({frente.numero})")
            else:
                print("  (la cola está vacía)")
        elif op == "5":
            num = leer_entero("  Número a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                print(f"  Encontrado en [{pos}]: {cola.datos[pos].nombre}")
            else:
                print("  No existe")
        elif op == "6":
            num = leer_entero("  Número de pasajero a modificar: ")
            if cola.buscar(num) != -1:
                n_destino = input("  Nuevo destino: ").strip()
                n_asiento = input("  Nuevo asiento: ").strip().upper()
                if cola.modificar(num, n_destino, n_asiento):
                    print("  ✓ Modificado correctamente")
            else:
                print("  No existe")
        elif op == "7":
            num = leer_entero("  Número de pasajero a eliminar: ")
            if cola.eliminar_por_numero(num):
                print(f"  ✓ Pasajero #{num} eliminado")
            else:
                print("  No existe")
        elif op == "8":
            copia = cola.copiar()
            print("  ✓ Copia creada:")
            copia.listar()
        elif op == "9":
            estado = "está vacía" if cola.esta_vacia() else "no está vacía"
            print(f"  Longitud: {cola.longitud()} · {estado}")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if cola.encolar(p):
                    cargados += 1
            print(f"  ✓ {cargados} datos de prueba encolados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()