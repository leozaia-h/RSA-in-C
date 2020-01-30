mport os
def chave_pub(x):
    arquivo = open('chave_publica_1.txt' , 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close()
    
def msg_criptografada(x):
    arquivo = open('msg_criptografada.txt', 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close
    
def msg_descriptografada(x):
    arquivo = open('msg_descriptografada.txt', 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close

def ler_chave_pub_1():
    arquivo = open('chave_publica_1.txt', 'r')
    x = arquivo.read()
    x = int(x)
    arquivo.close
    return(x)

def ler_chave_pub_2():
    arquivo = open('chave_publica_2.txt', 'r')
    y = arquivo.read()
    y = int(y)
    arquivo.close
    return(y)

def ler_msg_criptografada():
    arquivo = open('msg_criptografada.txt', 'r')
    x = arquivo.read()
    arquivo.close
    return x

def ler_msg_descriptografada():
    arquivo = open('msg_descriptografada.txt', 'r')
    x = arquivo.read()
    arquivo.close
    return x

                                                      ################# PRA CIMA SAO FUNÇOES DE TEXTO ###################

def limpar_terminal():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def verificar_primos(x):
    if(x <= 1):
        return False

    for c in range(2,x):
        if(x % c == 0):
            return False
    return True        

def criptografar(texto, e, n):
    encriptado = (texto ** e) % n
    return encriptado

def achar_d(e, phi):
    i = 1
    while(True):
        if(e * i % phi == 1):
            return i
        i += 1

def primos_entre_si(n,e):
    resultado = MDC(n, e)

    if(resultado == 1):
        return 1
    else:
        return 0

def calcular_phi(p, q):
    return (p - 1) * (q - 1)
    
def MDC(p, q):
    if(q == 0):
        return p
    else:
        return MDC(q, p%q)

def main():
        limpar_terminal()
        print("  ====================================================")
        print("  ==        ENCRIPTAÇÃO E DESENCRIPTAÇÃO RSA        ==")
        print("  ====================================================")
        print("  ==        Escolha uma das opções á seguir:        ==")
        print("  ==                                                ==")
        print("  == 1: GERAR CHAVE PUBLICA                         ==")
        print("  == 2: ENCRIPTAR                                   ==")
        print("  == 3: DESENCRIPTAR                                ==")
        print("  == 4: SAIR                                        ==")
        print("  ====================================================")
        escolha = int(input("  ## >Digite sua escolha: "))
        print("  ====================================================")
        limpar_terminal()

        if(escolha == 1):
            print("  ====================================================")
            print("  ==              Gerando chave pública             ==")
            print("  ====================================================")
            print("  == Digite os números primos:                      ==")
            p = int(input("  ## (p):"))
            q = int(input("  ## (q):"))
            if(verificar_primos(p) == False or verificar_primos(q) == False):
                    while(verificar_primos(p) == False or verificar_primos(q) == False):
                        limpar_terminal()
                        print("  ====================================================")
                        print("  ==  Um ou mais números digitados não são primos!  ==")
                        print("  ====================================================")
                        print("  ==  Digite novamente:                             ==")
                        p = int(input("  ##  Digite (p):"))
                        q = int(input("  ##  Digite (q):"))
            n = p * q
            phi = calcular_phi(p,q)
            print(" ======================================================")
            limpar_terminal()
            print("  =====================================================")
            print("  ==     INSIRA O e PARA GERAR A CHAVE PÚBLICA       ==")
            print("  =====================================================")
            e = int(input("  ## (e):     "))

            while(primos_entre_si(e,phi) == 0 or e >= phi or e <= 1):
                limpar_terminal()
                if(primos_entre_si(e, phi) == 0 and e < phi and e > 1):
                    print(" =====================================================")
                    print(" ==  O número digitado não é coprimo ao phi!        ==")
                    print(" =====================================================")
                    print("  ==  Digite novamente:                             ==")
                elif(e >= phi):
                    print(" =====================================================")
                    print(" ==  O número digitado é maior ou igual a phi!      ==")
                    print(" =====================================================")
                    print("  ==  Digite novamente:                             ==")
                elif(e <= 1):
                    print(" =====================================================")
                    print(" ==  O número digitado é menor ou igual a 1         ==")
                    print(" =====================================================")
                    print("  ==  Digite novamente:                             ==")

                e = int(input("  ## (e): "))
            print('Chave pública: {} {}'.format(n,e))
            chavePublica = str(N) + " " + str(e)
            chave_pub(chavePublica)
            #CHAVE PUBLICA SAI AQUI (ARQUIVO)
        elif(escolha == 2):
            limpar_terminal()
            print(" =====================================================")
            print("  ==     DIGITE A SUA MENSAGEM PARA ENCRIPTA-LA     ==")
            print(" =====================================================")
            texto = input("  ## > ")

            limpar_terminal()
            print(" =====================================================")
            print("  ==          PRECISAMOS DA CHAVE PUBLICA!          ==")
            print(" =====================================================")
            n = int(input("  ## (n): "))
            e = int(input("  ## (e): "))
            texto_encriptado = encriptar()
            #TEXTO ENCRIPTADO AQUI (ARQUIVO)
        elif(escolha == 3):
            pass
#----------------------------------------------
main()
