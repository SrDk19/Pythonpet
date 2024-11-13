import os

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def menu_principal():
    print("\n\t\tMENU MONSTRUOSO:")
    print("\t1. Cadastro")
    print("\t2. Atendimento")
    print("\t3. Consultas/Relatórios")
    print("\t4. Fazer Logout")
    print("\t5. Sair\n")
def menu_cadastro():
    limpar_terminal()
    print("\n\t1. Funcionários (ademiros)")
    print("\t2. Clientes")
    print("\t3. Pets")
    print("\t4. Serviços (ademiros)")
    print("\t5. Voltar ao Menu Principal\n")
def menu_usuarios():
    print("\n\t1. Cadastrar novo Funcionário")
    print("\t2. Fazer Login")
    print("\t3. Atualizar ")
    print("\t4. Apagar")
    print("\t5. Consultar")
    print("\t6. Voltar ao Menu Cadastro\n")
def menu_clientes():
    print("\n\t1. Cadastrar novo Cliente")
    print("\t2. Fazer Login")
    print("\t3. Atualizar")
    print("\t4. Apagar (ademiros)")
    print("\t5. Consultar")
    print("\t6. Voltar ao Menu Cadastro\n")
def menu_pets():
    print("\n\t1. Cadastrar novo Pet")
    print("\t2. Atualizar ")
    print("\t3. Apagar (ademiros)")
    print("\t4. Consultar")
    print("\t5. Voltar ao Menu Cadastro\n")
def menu_servicos():
    print("\n\t1. Cadastrar novo Serviço (ademiros)")
    print("\t2. Atualizar (ademiros)")
    print("\t3. Apagar (ademiros)")
    print("\t4. Consultar (ademiros)")
    print("\t5. Voltar ao Menu Cadastro\n")
def menu_atendimento():
    print("\n\t1. Iniciar")
    print("\t2. Agendar")
    print("\t3. Remarcar")
    print("\t4. Voltar ao Menu Principal\n")
def menu_consultas():
    print("\n\t1. Consulta/relatorio")
    print("\t2. Voltar ao Menu Principal\n")
