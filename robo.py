from automato import Automato

def criar_robo():
    estados = {"R_Base", "R_Plan", "R_Mina", "R_MinaC", "R_PlanC", "R_BaseC", "R_Entregue"}
    alfabeto = {"A", "R", "C", "D", "E"}
    programa = {
        ("R_Base", "A"): "R_Plan",
        ("R_Plan", "A"): "R_Mina",
        ("R_Plan", "R"): "R_Base",
        ("R_Mina", "R"): "R_Plan",
        ("R_Mina", "C"): "R_MinaC",
        ("R_MinaC", "R"): "R_PlanC",
        ("R_PlanC", "R"): "R_BaseC",
        ("R_BaseC", "D"): "R_Entregue",
        ("R_Entregue", "A"): "R_Plan",
    }

    for estado in estados:
        programa[(estado, "E")] = estado

    return Automato(alfabeto, estados, programa, "R_Base", {"R_Entregue"})
