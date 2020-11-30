import os
import math
from Funcoes.funcionalidades import *
from Funcoes.GUI import *

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
