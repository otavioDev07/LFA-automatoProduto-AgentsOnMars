from robo import criar_robo
from alien import criar_alien
from automatoProduto import AutomatoProduto

def main():
    robo = criar_robo()
    alien = criar_alien()
    produto = AutomatoProduto(robo, alien)

    produto.gerar_produto()

    print("Estados:", len(produto.estados))
    print("Transições:", len(produto.programa))
    print("Estados finais:", len(produto.estadosFinais))

    while True:
        palavra = input("entre com uma palavra válida ou SAIR para encerrar: \n").strip().upper()
        if palavra == "SAIR": break
        produto.testarPalavra(palavra)
    
    
if __name__ == "__main__":
    main()