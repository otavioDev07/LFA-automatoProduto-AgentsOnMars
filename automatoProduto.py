
from collections import deque

class AutomatoProduto:
    def __init__(self, robo, alien):
        self.robo = robo
        self.alien = alien
        self.estadoInicial = (robo.estadoInicial, alien.estadoInicial)

        self.estados = {self.estadoInicial}
        self.programa = {}
        self.estadosFinais = set()

    def lerEntrada(self, estado, simbolo):
        estadoRobo, estadoAlien = estado

        novoRobo = self.robo.lerEntrada(estadoRobo, simbolo)
        novoAlien = self.alien.lerEntrada(estadoAlien, simbolo)

        if novoRobo is None or novoAlien is None: return "TRANSIÇÃO INVÁLIDA"

        if novoAlien == "A_Plan" and novoRobo in {"R_Plan", "R_PlanC"}: return "ROBÔ CAPTURADO"

        return (novoRobo, novoAlien)

    def gerar_produto(self):
        fila = deque([self.estadoInicial])

        while fila:
            estadoAtual = fila.popleft()

            estadoRobo, estadoAlien = estadoAtual

            if (estadoRobo in self.robo.estadosFinais and estadoAlien in self.alien.estadosFinais): self.estadosFinais.add(estadoAtual)

            for simbolo in self.robo.alfabeto:
                proximoEstado = self.lerEntrada(estadoAtual, simbolo)

                if proximoEstado in ("TRANSIÇÃO INVÁLIDA", "ROBÔ CAPTURADO"): continue

                self.programa[(estadoAtual, simbolo)] = proximoEstado

                if proximoEstado not in self.estados:
                    self.estados.add(proximoEstado)
                    fila.append(proximoEstado)

    def testarPalavra(self, palavra):
        estadoAtual = self.estadoInicial

        print(f"\nEstado inicial: {estadoAtual}\n")

        for simbolo in palavra:
            proximoEstado = self.lerEntrada(estadoAtual, simbolo)

            print(f"({estadoAtual}, {simbolo}) => {proximoEstado}")

            if proximoEstado in ("TRANSIÇÃO INVÁLIDA", "ROBÔ CAPTURADO"):
                print("\nPalavra REJEITADA!")
                return False

            estadoAtual = proximoEstado

        if estadoAtual in self.estadosFinais:
            print(f"\nEstado final alcançado: {estadoAtual}")
            print("Palavra ACEITA!")
            return True

        print(f"\nEstado alcançado: {estadoAtual}")
        print("Palavra REJEITADA!")
        return False
