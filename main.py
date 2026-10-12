from robo import criar_robo
from alien import criar_alien

def main():
    robo = criar_robo()
    alien = criar_alien()

    print(robo.lerEntrada("R_Base", "A"))
    print(robo.lerEntrada("R_Mina", "C"))
    print(robo.lerEntrada("R_Mina", "E"))

    print(alien.lerEntrada("A_Cav1", "A"))
    print(alien.lerEntrada("A_Cav2", "E"))
    print(alien.lerEntrada("A_Plan", "R"))

if __name__ == "__main__":
    main()