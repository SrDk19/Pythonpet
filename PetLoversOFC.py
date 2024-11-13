from funcoesmenu import *
from funcoescadastro import *
from funcaocliente import *
from funcaofinal import *
from funcaoservico import *
import time

usuario_logado = None
tipo = None

def variavel():
    global tipo

def logout():
    global usuario_logado, tipo
    usuario_logado = None
    tipo = None
    print("Logout realizado com sucesso. Até mais eu acho...")
    time.sleep(2)
    limpar_terminal()

while True:
    menu_principal()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        limpar_terminal()
        while True:
            menu_cadastro()
            opcao_cadastro = int(input("Escolha a opção de cadastro: "))

            if opcao_cadastro:
                while True:
                    menu_usuarios()
                    opcao_usuario = int(input("Escolha a opção de Funciónario: "))
                    if opcao_usuario == 1 and tipo == 'A':
                        cadastro_usuarios()
                    elif opcao_usuario == 2:
                        tipo = login_usuario()
                        if tipo:
                            print(f"Tipo de usuário logado: {tipo}")
                        else:
                            print("Falha no login, tente novamente.")
                    elif opcao_usuario == 3 and tipo == 'A':
                        usuario_atualizar()
                    elif opcao_usuario == 4 and tipo == 'A':
                        apagar_usuario()
                    elif opcao_usuario == 5 and tipo == 'A':
                        consultar_usuarios()
                    elif opcao_usuario == 6:
                        break
                    else: 
                        print("Opção inválida, por favor tente novamente.")
            elif opcao_cadastro == 2:
                limpar_terminal()
                while True:
                    menu_clientes()
                    opcao_usuario = int(input("Escolha a opção de Clientes: "))
                    if opcao_usuario == 1:
                        cadastro_clientes()
                    elif opcao_usuario == 2:
                        tipo = login_clientes()
                        if tipo:
                            print(f"Tipo de usuário logado: {tipo}")
                        else:
                            print("Falha no login, tente novamente.")
                    elif opcao_usuario == 3:
                        clientes_atualizar()
                    elif opcao_usuario == 4 and tipo == 'A':
                        apagar_cliente()
                    elif opcao_usuario == 5:
                        consultar_cliente()
                    elif opcao_usuario == 6:
                        break
                    else: 
                        print("Opção inválida, por favor tente novamente.")

            elif opcao_cadastro == 3:
                limpar_terminal()
                while True:
                    menu_pets()
                    opcao_pets = int(input("Escolha a opção de Pets: "))
                    if opcao_pets == 1:
                        cadastrar_pet()
                    elif opcao_pets == 2:
                        atualizar_pet()
                    elif opcao_pets == 3 and tipo == 'A':
                        apagar_pet()
                    elif opcao_pets == 4:
                        consultar_pet()
                    elif opcao_pets == 5:
                        break
                    else: 
                        print("Opção inválida, por favor tente novamente.")

            elif opcao_cadastro == 4:
                limpar_terminal()
                if tipo == 'A':
                    while True:
                        menu_servicos()
                        opcao_servicos = int(input("Escolha a opção de Serviços: "))
                        if opcao_servicos == 1:
                            cadastrar_servico()
                        elif opcao_servicos == 2:
                            atualizar_servico()
                        elif opcao_servicos == 3:
                            apagar_servico()
                        elif opcao_servicos == 4:
                            consultar_servico()
                        elif opcao_servicos == 5:
                            break
                        else: 
                            print("Opção inválida, por favor tente novamente.")
                else:
                    print("Você não tem permissão para acessar isso KKKK, seu beta.")

            elif opcao_cadastro == 5:
                limpar_terminal()
                break
            else: 
                print("Opção inválida, por favor tente novamente.")
    
    elif opcao == 2:
        limpar_terminal()
        while True:
            menu_atendimento()
            opcao_atendimento = int(input("Escolha a opção de atendimento: "))
            if opcao_atendimento == 1:
                iniciar_atendimento()
            elif opcao_atendimento == 2:
                agendar_atendimento()
            elif opcao_atendimento == 3:
                remarcar_atendimento()
            elif opcao_atendimento == 4:
                break
            else:
                print("Opção inválida, por favor tente novamente.")

    elif opcao == 3:
        limpar_terminal()
        while True:
            menu_consultas()
            opcao_consulta = int(input("Escolha a opção de consultas: "))
            
            if opcao_consulta == 1:
                consulta_relatorio_1()
            elif opcao_consulta == 2:
                break
            else:
                print("Opção inválida, por favor tente novamente.")
    elif opcao == 4:
        limpar_terminal()
        logout()
        print("Logout realizado com sucesso.")
        time.sleep(3)

    elif opcao == 5:
        limpar_terminal()
        print("Leaving.png")
        time.sleep(2)
        limpar_terminal()
        break
    else:
        print("Opção inválida, por favor tente novamente.")