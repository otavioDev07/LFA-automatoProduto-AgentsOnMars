from automato import Automato

class AutomatoProduto:
    def __init__(self, robo, alien):
        self.robo = robo
        self.alien = alien
        self.estadoInicial = (robo.estadoInicial, alien.estadoInicial)

    def lerEntrada(self, estado, simbolo):
        estadoRobo, estadoAlien = estado
        novoRobo = self.robo.lerEntrada(estadoRobo, simbolo)
        novoAlien = self.alien.lerEntrada(estadoAlien, simbolo)

        if novoRobo is None or novoAlien is None: return None
        if novoAlien == "A_Plan" and novoRobo in {"R_Plan", {"R_PlanC"}}: return None

        return (novoRobo, novoAlien)