def main_GUI():
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

def digitar_chavePub_GUI():
    print("  <==================================================>")
    print("  <=              GERANDO CHAVE PÚBLICA             =>")
    print("  <==================================================>")
    print("  <= Digite os números primos:                      =>")
    print("  <==================================================>")

def erro_pq_pequenos_GUI():
    print("  <==================================================>")
    print("  <=          (p) e (q) são muito pequenos!         =>")
    print("  <=              Digite-os novamente!              =>")
    print("  <==================================================>")

def erro_nao_primos_GUI():
    print("  <==================================================>")
    print("  <=  Um ou mais números digitados não são primos!  =>")
    print("  <=              Digite-os novamente!              =>")
    print("  <==================================================>")

def erro_pq_iguais_GUI():
    print("  <==================================================>")
    print("  <=             (p) e (q) são iguais!              =>")
    print("  <=              Digite-os novamente!              =>")
    print("  <==================================================>")
    
def digitar_e_GUI():
    print("  <==================================================>")
    print("  <=    Insira o (e) para gerar a chave pública:    =>")
    print("  <==================================================>")

def erro_coprimo_phi_GUI():
    print("  <==================================================>")
    print("  <=     O NÚMERO DIGITADO NÃO É COPRIMO A PHI!     =>")
    print("  <=              Digite (e) novamente:             =>")
    print("  <==================================================>")

def erro_maior_phi_GUI():
    print("  <==================================================>")
    print("  <=    O NÚMERO DIGITADO É MAIOR OU IGUAL A PHI!   =>")
    print("  <=              Digite (e) novamente:             =>")
    print("  <==================================================>")

def erro_menor_1_GUI():
    print("  <==================================================>")
    print("  <=     O NÚMERO DIGITADO É MENOR OU IGUAL A 1!    =>")
    print("  <=              Digite (e) novamente:             =>")
    print("  <==================================================>")

def print_GenchavPub_GUI(n, e):
    print("  ####################################################")
    print("  >>CHAVE PÚBLICA: (n):{} (e):{}                      ".format(n, e))
    print("  ####################################################")

def digitar_chavePub_n_e_GUI():
    print("  <==================================================>")
    print("  <=          PRECISAMOS DA CHAVE PUBLICA!          =>")
    print("  <=              Digite o (n) e o (e)              =>")
    print("  <==================================================>")

def digitar_msg_GUI():
    print("  <==================================================>")
    print("  <=    Digite a sua mensagem para encripta-la:     =>")
    print("  <==================================================>")

def alert_msg_arq():
    print("  ####################################################")
    print("           SUA MENSAGEM SE ENCONTRA NO ARQUIVO        ")
    print("                  msg_criptografada.txt               ")
    print("  ####################################################")

def quest_txtext_GUI():
    print("  <==================================================>")
    print("  <=       Deseja utilizar um arquivo externo?      =>")
    print("  <=              (1)Sim      (2)Não                =>")
    print("  <==================================================>")

def digitar_novo_arq_GUI():
    print("  <==================================================>")
    print("  <=       Digite o nome do arquivo que deseja      =>")
    print("  <=                  desencriptar:                 =>")
    print("  <==================================================>")

def erro_escInvalida_GUI():
    print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
    print("  <!!               Escolha inválida               !!>")
    print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")

def digitar_pqe_GUI():
    print("  <==================================================>")
    print("  <=     Para desencriptar insira os valores de:    =>")
    print("  <=                 (p), (q) e (e)                 =>")
    print("  <==================================================>")

def alert_saidaArquivo_GUI():
    print("  ####################################################")
    print("           SUA MENSAGEM SE ENCONTRA NO ARQUIVO        ")
    print("                msg_descriptografada.txt              ")
    print("  ####################################################")
