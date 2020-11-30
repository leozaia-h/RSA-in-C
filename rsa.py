import os
import math
from GUI import *

def inverso(e, phi):


    phi2 = phi
    coeficientes = [] 
    coeficientes_invertidos = []
    indices = []

    tamanho=0
    tabela = 1

    a = e/phi
    a = int(a)
    coeficientes.append(a)
    b = e%phi

    while(b!=0):
        e = phi
        phi = b
        a = e/phi
        a = int(a)
        b = e%phi
        
        coeficientes.append(a)
        tamanho += 1
   
    j=tamanho-1

    for i in range(0,tamanho):
        coeficientes_invertidos.append(coeficientes[j])
        j -= 1

    tabela = 1
    anterior = 0

    for i in range(0,tamanho):
        indices.append(coeficientes_invertidos[i]*tabela + anterior)
        anterior = tabela
        tabela = indices[i]
  
    if(tamanho % 2 == 0):
        indices[tamanho-2] = -indices[tamanho-2]
        while(indices[tamanho-2]<1):
            indices[tamanho-2] = indices[tamanho-2] + phi2

    inv = indices[tamanho-2]
    return inv

def fastModularExponentiation(m, e, n):
    if(e == 0):
        return 1
    elif(e%2 == 0):
        aux = fastModularExponentiation(m, e/2, n)
        return (aux**2)%n
    else:
        return(m%n*fastModularExponentiation(m, e-1, n))%n

def limpar_terminal():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def limpar_arquivo(apagar):

    arquivo = open(apagar, 'w')
    arquivo.close()

def verificar_primos(x):
    if(x <= 1):
        return False
    aux = math.ceil(math.sqrt(x))
    for i in range(2,aux):
        if(x % i == 0):
            return False
    return True

def primos_entre_si(n,e):
    resultado = MDC(n, e)

    if(resultado == 1):
        return True
    else:
        return False
def MDC(p, q):
    if(q == 0):
        return p
    else:
        return MDC(q, p%q)

def calcular_phi(p, q):
    return (p - 1) * (q - 1)

def chave_pub(x):
    arquivo = open('chave_publica.txt' , 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close()

def msg_criptografada(x):
    arquivo = open('msg_criptografada.txt', 'a')
    arquivo.write("{} ".format(x))
    arquivo.close()
    
def msg_descriptografada(x): 
    arquivo = open('msg_descriptografada.txt', 'a')
    arquivo.write("{}\n".format(x))
    arquivo.close()

def criptografar(c,e,n):
    array = ['@','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    aux = 0
    for i in range(0,29):
        if(c == array[i]):
            aux = i
    M = fastModularExponentiation(aux, e, n)
    return M

def desencriptar(nome_arquivo, d, n):
    array = ['@','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

    arquivo = open(nome_arquivo, 'r')
    msg = arquivo.read().split(" ")
    palavras = ""
    tamanho = msg.__len__()
    tamanho -= 1
    
    for i in range (0, tamanho):
        if(msg[i] == " "):
            break
        c = msg[i]
        c = int(c)
        c = fastModularExponentiation(c, d, n)
        palavras += array[c]
        
    msg_descriptografada(palavras)
    arquivo.close()

def main():
    limpar_terminal()
    while(1):
        main_GUI()
        escolha = int(input("    >Digite sua escolha: " ))
        limpar_terminal()
    
        if(escolha == 1):
            digitar_chavePub_GUI()
            p = int(input("     (p):"))
            q = int(input("     (q):"))
            if(p * q < 28):
                while(p * q < 28):
                    erro_pq_pequenos_GUI()
                    p = int(input("      Digite (p):"))
                    q = int(input("      Digite (q):"))
            if(verificar_primos(p) == False or verificar_primos(q) == False):
                    while(verificar_primos(p) == False or verificar_primos(q) == False):
                        limpar_terminal()
                        erro_nao_primos_GUI()
                        p = int(input("      Digite (p):"))
                        q = int(input("      Digite (q):"))
            if(p == q):
                    while(p == q):
                        limpar_terminal()
                        erro_pq_iguais_GUI()
                        p = int(input("      Digite (p):"))
                        q = int(input("      Digite (q):"))
            n = p * q
            phi = calcular_phi(p, q)
            limpar_terminal()
            digitar_e_GUI()
            e = int(input("     (e): "))
            while(primos_entre_si(e,phi) == 0 or e >= phi or e <= 1):
                limpar_terminal()
                if(primos_entre_si(e, phi) == 0 and e < phi and e > 1):
                    erro_coprimo_phi_GUI()
                elif(e >= phi):
                    erro_maior_phi_GUI()
                elif(e <= 1):
                    erro_menor_1_GUI()

                e = int(input("     (e): "))
            limpar_terminal()
            print_GenchavPub_GUI(n, e)

            chave = str(n) +" "+ str(e)
            chave_pub(chave)

        elif(escolha == 2):
            limpar_terminal()
            digitar_chavePub_n_e_GUI()
            n = int(input("     (n): "))
            e = int(input("     (e): "))
            digitar_msg_GUI()

            texto = input("    > ")
            texto = texto.upper()

            limpar_terminal()
            alert_msg_arq()
            limpar_arquivo('msg_criptografada.txt')
            
            for i in range(0,len(texto)):
                msg_criptografada(criptografar(texto[i], e, n))
            print()
    
        elif(escolha == 3):
            limpar_terminal()
            while(1):
                quest_txtext_GUI()
                escolha = int(input("    > "))
                if(escolha == 1):
                    digitar_novo_arq_GUI()
                    nome_arquivo = input("    Arquivo: ")
                    break
                elif(escolha == 2):
                    nome_arquivo = "msg_criptografada"
                    break
                else:
                    erro_escInvalida_GUI()
                    
            digitar_pqe_GUI()
            p = int(input("    (p): "))
            q = int(input("    (q): "))
            e = int(input("    (e): "))

            limpar_terminal()
            alert_saidaArquivo_GUI()

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
            erro_escInvalida_GUI()
main()
