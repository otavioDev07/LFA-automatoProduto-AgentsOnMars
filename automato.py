class Automato:
    def __init__(self, alfabeto, estados, programa, estadoInicial, estadosFinais):
        self.alfabeto = alfabeto
        self.estados = estados
        self.programa = programa
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais

    def lerEntrada(self, estado, simbolo):
        return self.programa.get((estado, simbolo))
