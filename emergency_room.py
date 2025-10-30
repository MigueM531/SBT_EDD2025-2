from Arbol import *
from queue import *

class Paciente:
    orden = 0
    def __init__(self, id, nombre, nivel_emergencia):
        Paciente.orden += 1
        self.id = id
        self.nombre = nombre
        self.nivel_emergencia: int = nivel_emergencia
        self.orden_llegada = Paciente.orden

    def __lt__(self, other):
        if self.nivel_emergencia == other.nivel_emergencia:
            return self.orden_llegada < other.orden_llegada
        return self.nivel_emergencia < other.nivel_emergencia

    def __str__(self):
        return f"{self.nombre} [PRIORIDAD: {self.nivel_emergencia} - LLEGADA: {self.orden_llegada}]"


class Quirofano:
    def __init__(self):
        self.root = None


    def registrar_paciente(self, paciente):
        nuevo_nodo = BinaryTreeNode(paciente)

        if self.root is None:
            self.root = nuevo_nodo
            return

        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            actual = q.dequeue()

            if actual.leftchild is None:
                actual.leftchild = nuevo_nodo
                nuevo_nodo.parent = actual
                self.heap_up(nuevo_nodo)
                return

            elif actual.rightchild is None:
                actual.rightchild = nuevo_nodo
                nuevo_nodo.parent = actual
                self.heap_up(nuevo_nodo)
                return

            q.enqueue(actual.leftchild)
            q.enqueue(actual.rightchild)


    def heap_up(self, nodo):
        while nodo.parent and nodo.data < nodo.parent.data:
            nodo.data, nodo.parent.data = nodo.parent.data, nodo.data
            nodo = nodo.parent


    def consultar_siguiente(self):
        if self.root is not None:
            return self.root.data
        
    
    def programar_cirugia(self):
        if self.root is None:
            return None

        paciente_siguiente = self.root.data

        if self.root.leftchild is None and self.root.rightchild is None:
            self.root = None
            return paciente_siguiente

        q = Queue()
        q.enqueue(self.root)
        ultimo = None
        padre_ultimo = None

        while not q.is_empty():
            actual = q.dequeue()
            if actual.leftchild:
                padre_ultimo = actual
                q.enqueue(actual.leftchild)
            if actual.rightchild:
                padre_ultimo = actual
                q.enqueue(actual.rightchild)
            ultimo = actual


        self.root.data = ultimo.data

        if padre_ultimo.rightchild == ultimo:
            padre_ultimo.rightchild = None
        else:
            padre_ultimo.leftchild = None

        self.heap_down(self.root)

        print(f"{paciente_siguiente.nombre} será llevado a cirugía.")
        return paciente_siguiente

    def heap_down(self, nodo):
        if nodo is None:
            return

        menor = nodo

        if nodo.leftchild and nodo.leftchild.data < menor.data:
            menor = nodo.leftchild
        if nodo.rightchild and nodo.rightchild.data < menor.data:
            menor = nodo.rightchild

        if menor != nodo:
            nodo.data, menor.data = menor.data, nodo.data
            self.heap_down(menor) 


    def ver_lista_pacientes(self):
        if self.root is None:
            print("No hay pacientes en espera.")
            return

        q = Queue()
        q.enqueue(self.root)


        while not q.is_empty():
            nodo = q.dequeue()
            p = nodo.data

            print(p)

            if nodo.leftchild:
                q.enqueue(nodo.leftchild)
            if nodo.rightchild:
                q.enqueue(nodo.rightchild)

    def ver_pacientes_prioridad(self, nivel_emergencia):
        if self.root is None:
            print("No hay pacientes en espera.")
            return

        q = Queue()
        q.enqueue(self.root)
        encontrados = 0

        while not q.is_empty():
            nodo = q.dequeue()
            p = nodo.data

            if p.nivel_emergencia == nivel_emergencia:
                print(p)
                encontrados += 1

            if nodo.leftchild:
                q.enqueue(nodo.leftchild)
            if nodo.rightchild:
                q.enqueue(nodo.rightchild)

        if encontrados == 0:
            print("No se encontraron pacientes con este nivel de emergencia.\n")
        else:
            print(f"Total encontrados: {encontrados}\n")


quirofano = Quirofano()

quirofano.registrar_paciente(Paciente(1, "Ana", 2))
quirofano.registrar_paciente(Paciente(2, "Luis", 1))
quirofano.registrar_paciente(Paciente(3, "Marta", 4))
quirofano.registrar_paciente(Paciente(4, "Carlos", 1))
quirofano.registrar_paciente(Paciente(5, "Andres", 3))

print("\n=== Árbol de pacientes ===")
printTree(quirofano.root)

print(f"\nSIGUIENTE A QUIROFANO: {quirofano.consultar_siguiente()}")

print("\n=== Paciente en cirugía ===")
atendido = quirofano.programar_cirugia()
print(f"Se atendió a: {atendido}")

print("\n=== Árbol de pacientes ===")
printTree(quirofano.root)

print(f"\nSIGUIENTE A QUIROFANO: {quirofano.consultar_siguiente()}")

print(f"\n=== ORDEN ARBOL ===")
quirofano.ver_lista_pacientes()

print(f"\n=== VER POR PRIORIDAD ===")
quirofano.ver_pacientes_prioridad(1)
