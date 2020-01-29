import random

def ver_primo(x):
    if(x == 1):
        return True
    else:
        return False

def limpar_terminal():
    for i in range(1, 40):
        print()

def calcular_totiente():
    return 1

def verificar_coprimos(x):
    if(x == 1):
        return True
    else:
        return False

def main():
    limpar_terminal()
    print("  ####################################################")
    print("  ##        ENCRIPTAÇÃO E DESENCRIPTAÇÃO RSA        ##")
    print("  ####################################################")
    print("  ##        Escolha uma das opções á seguir:        ##")
    print("  ##                                                ##")
    print("  ## 1: GERAR CHAVE PUBLICA                         ##")
    print("  ## 2: ENCRIPTAR                                   ##")
    print("  ## 3: DESENCRIPTAR                                ##")
    print("  ## 4: SAIR                                        ##")
    print("  ####################################################")
    escolha = int(input("     >Digite sua escolha: "))
    limpar_terminal()

    if(escolha == 1):
        print("  ####################################################")
        print("  ##              Gerando chave pública             ##")
        print("  ####################################################")
        print("  ## Digite os números primos:                      ##")
        print("  ####################################################")
        p = int(input("     (p):"))
        q = int(input("     (q):"))
        if(ver_primo(p) == False or ver_primo(q) == False):
                while(ver_primo(p) != True and ver_primo(q) != True):
                    limpar_terminal()
                    print("  ####################################################")
                    print("  ##  Um ou mais números digitados não são primos!  ##")
                    print("  ##              Digite-os novamente!              ##")
                    print("  ####################################################")
                    p = int(input("      Digite (p):"))
                    q = int(input("      Digite (q):"))
        n = p * q
        totiente = calcular_totiente()
        limpar_terminal()
        print("  ####################################################")
        print("  ##     INSIRA O e PARA GERAR A CHAVE PÚBLICA      ##")
        print("  ####################################################")
        e = int(input("     (e): "))
        if(verificar_coprimos(e) != 1):
            while(verificar_coprimos(e) != 1):
                limpar_terminal()
                print("  ####################################################")
                print("  ##  O número digitado não é coprimo ao totiente!  ##")
                print("  ####################################################")
                print("  ##  Digite novamente:                             ##")
                e = int(input("     (e): "))
    elif(escolha == 2):
        limpar_terminal()
        print("  ====================================================")
        print("  ##     DIGITE A SUA MENSAGEM PARA ENCRIPTA-LA     ##")
        print("  ====================================================")
        texto = input("  ## > ")
        limpar_terminal()
        print("  ####################################################")
        print("  ##          PRECISAMOS DA CHAVE PUBLICA!          ##")
        print("  ####################################################")
        n = int(input("  ## (n): "))
        e = int(input("  ## (e): "))
        texto_encriptado = encriptar()
main()
