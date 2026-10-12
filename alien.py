from automato import Automato

def criar_alien():
    estados = {"A_Cav1", "A_Cav2", "A_Plan"}
    alfabeto = {"A", "R", "C", "D", "E"}

    ciclo = {
        "A_Cav1": "A_Cav2",
        "A_Cav2": "A_Plan",
        "A_Plan": "A_Cav1"
    }

    programa = {}

    for estado, destino in ciclo.items():
        for simbolo in alfabeto:
            programa[(estado, simbolo)] = destino

    return Automato(alfabeto, estados, programa, "A_Cav1", estados)

    