def main():
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
            n = p * q
            phi = calcular_phi(p, q)
            limpar_terminal()
            print("  <==================================================>")
            print("  <=    INSIRA O (e) PARA GERAR A CHAVE PÚBLICA     =>")
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
        elif(escolha == 2):
            limpar_terminal()
            print("  <==================================================>")
            print("  <=     DIGITE A SUA MENSAGEM PARA ENCRIPTA-LA     =>")
            print("  <==================================================>")
            texto = input("    > ")
            limpar_terminal()
            print("  <==================================================>")
            print("  <=          PRECISAMOS DA CHAVE PUBLICA!          =>")
            print("  <=              Digite o (n) e o (e)              =>")
            print("  <==================================================>")
            n = int(input("  == (n): "))
            e = int(input("  == (e): "))
    
        elif(escolha == 3):
            limpar_terminal()
            print("  <==================================================>")
            print("  <=     PARA DESENCRIPTAR INSIRA OS VALORES DE:    =>")
            print("  <=                 (p), (q) e (e)                 =>")
            print("  <==================================================>")
            p = int(input("    (p): "))
            q = int(input("    (q): "))
            e = int(input("    (e): "))
    
        elif(escolha == 4):
            exit()
        else:
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
            print("  <!!               Escolha inválida               !!>")
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
main()
