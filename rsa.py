import os
import math
from Funcoes.funcionalidades import *

def main():
    limpar_terminal()
    while(1):
        print("  <==================================================>")
        print("  <=        ENCRIPTAÇÃO E DESENCRIPTAÇÃO RSA        =>")
        print("  <==================================================>")
        print("  <=        Escolha uma das opções á seguir:        =>")
        print("  <=                                                =>")
        print("  <= 1: GERAR CHAVE PUBLICA                         =>")
        print("  <= 2: ENCRIPTAR                                   =>")
        print("  <= 3: DESENCRIPTAR                                =>")
        print("  <= 4: SAIR                                        =>")
        print("  <==================================================>")
        escolha = int(input("    >Digite sua escolha: " ))
        limpar_terminal()
    
        if(escolha == 1):
            print("  <==================================================>")
            print("  <=              GERANDO CHAVE PÚBLICA             =>")
            print("  <==================================================>")
            print("  <= Digite os números primos:                      =>")
            print("  <==================================================>")
            p = int(input("     (p):"))
            q = int(input("     (q):"))
            if(p * q < 28):
                while(p * q < 28):
                    print("  <==================================================>")
                    print("  <=          (p) e (q) são muito pequenos!         =>")
                    print("  <=              Digite-os novamente!              =>")
                    print("  <==================================================>")
                    p = int(input("      Digite (p):"))
                    q = int(input("      Digite (q):"))
            if(verificar_primos(p) == False or verificar_primos(q) == False):
                    while(verificar_primos(p) == False or verificar_primos(q) == False):
                        limpar_terminal()
                        print("  <==================================================>")
                        print("  <=  Um ou mais números digitados não são primos!  =>")
                        print("  <=              Digite-os novamente!              =>")
                        print("  <==================================================>")
                        p = int(input("      Digite (p):"))
                        q = int(input("      Digite (q):"))
            if(p == q):
                    while(p == q):
                        limpar_terminal()
                        print("  <==================================================>")
                        print("  <=             (p) e (q) são iguais!              =>")
                        print("  <=              Digite-os novamente!              =>")
                        print("  <==================================================>")
                        p = int(input("      Digite (p):"))
                        q = int(input("      Digite (q):"))
            n = p * q
            phi = calcular_phi(p, q)
            limpar_terminal()
            print("  <==================================================>")
            print("  <=    Insira o (e) para gerar a chave pública:    =>")
            print("  <==================================================>")
            e = int(input("     (e): "))
            while(primos_entre_si(e,phi) == 0 or e >= phi or e <= 1):
                limpar_terminal()
                if(primos_entre_si(e, phi) == 0 and e < phi and e > 1):
                    print("  <==================================================>")
                    print("  <=     O NÚMERO DIGITADO NÃO É COPRIMO A PHI!     =>")
                    print("  <=              Digite (e) novamente:             =>")
                    print("  <==================================================>")
                elif(e >= phi):
                    print("  <==================================================>")
                    print("  <=    O NÚMERO DIGITADO É MAIOR OU IGUAL A PHI!   =>")
                    print("  <=              Digite (e) novamente:             =>")
                    print("  <==================================================>")
                elif(e <= 1):
                    print("  <==================================================>")
                    print("  <=     O NÚMERO DIGITADO É MENOR OU IGUAL A 1!    =>")
                    print("  <=              Digite (e) novamente:             =>")
                    print("  <==================================================>")
    
                e = int(input("     (e): "))
            limpar_terminal()
            print("  ####################################################")
            print("              CHAVE PÚBLICA: (n):{} (e):{}            ".format(n, e))
            print("  ####################################################")
            
            chave = str(n) +" "+ str(e)
            chave_pub(chave)

        elif(escolha == 2):
            limpar_terminal()
            print("  <==================================================>")
            print("  <=          PRECISAMOS DA CHAVE PUBLICA!          =>")
            print("  <=              Digite o (n) e o (e)              =>")
            print("  <==================================================>")
            n = int(input("     (n): "))
            e = int(input("     (e): "))
            print("  <==================================================>")
            print("  <=    Digite a sua mensagem para encripta-la:     =>")
            print("  <==================================================>")

            texto = input("    > ")
            texto = texto.upper()

            limpar_terminal()

            print("  ####################################################")
            print("           SUA MENSAGEM SE ENCONTRA NO ARQUIVO        ")
            print("                  msg_criptografada.txt               ")
            print("  ####################################################")
    
            limpar_arquivo('msg_criptografada.txt')
            
            for i in range(0,len(texto)):
                msg_criptografada(criptografar(texto[i], e, n))
            print()
    
        elif(escolha == 3):
            limpar_terminal()
            while(1):
                print("  <==================================================>")
                print("  <=       Deseja utilizar um arquivo externo?      =>")
                print("  <=              (1)Sim      (2)Não                =>")
                print("  <==================================================>")
                escolha = int(input("    > "))
                if(escolha == 1):
                    print("  <==================================================>")
                    print("  <=       Digite o nome do arquivo que deseja      =>")
                    print("  <=                  desencriptar:                 =>")
                    print("  <==================================================>")
                    nome_arquivo = input("    Arquivo: ")
                    break
                elif(escolha == 2):
                    nome_arquivo = "msg_criptografada"
                    break
                else:
                    print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
                    print("  <!!               Escolha inválida               !!>")
                    print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
                    
            print("  <==================================================>")
            print("  <=     Para desencriptar insira os valores de:    =>")
            print("  <=                 (p), (q) e (e)                 =>")
            print("  <==================================================>")
            p = int(input("    (p): "))
            q = int(input("    (q): "))
            e = int(input("    (e): "))
            limpar_terminal()

            print("  ####################################################")
            print("           SUA MENSAGEM SE ENCONTRA NO ARQUIVO        ")
            print("                msg_descriptografada.txt              ")
            print("  ####################################################")

            phi = calcular_phi(p, q)
            n = p * q
            d = inverso(e, phi)

            nome_arquivo += '.txt'
            
            limpar_arquivo('msg_descriptografada.txt')
            desencriptar(nome_arquivo, d, n)
            
            print()
            
        elif(escolha == 4):
            exit()
        else:
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
            print("  <!!               Escolha inválida               !!>")
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
main()
