import os
import math

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
