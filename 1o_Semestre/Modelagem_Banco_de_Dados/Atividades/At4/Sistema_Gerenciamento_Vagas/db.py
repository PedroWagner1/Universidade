import pymysql

'''

!!!     ATENÇÃO   !!!

    Para o sistema rodar corretamente, é imprescendível que se adicione em um mysql-server a estrutura provida no arquivo estrutura_bd.sql



'''


#   Lembrando: A máquina que rodar o programa deve ter uma instância em localhost rodando mysql-server com os argumentos abaixos aplicáveis: (modifique conforme sua instância)
conexao = pymysql.connect(host='127.0.0.1', user='root', password='P@ssFlow', database='sistema_gerenciamento')
cursor = conexao.cursor()



    #   Adiciona Cliente
def adicionar_cliente(cpf, nome, data_nas, gestante, deficiente):

    try:
        cursor.execute("INSERT INTO Cliente(CPF, Nome, Data_Nasc, Gestante, Deficiente) VALUES(%s, %s, %s, %s, %s);", (cpf, nome, data_nas, gestante, deficiente))
        conexao.commit()
        return True
    except Exception as e:
        
        return False
    




def lista_clientes():

    cursor.execute('SELECT * FROM Cliente;')
    retorno = cursor.fetchall()
    lista = ['Nenhum']

    for tupla in retorno:
        valores = []
        for x in tupla:

            if isinstance(x, str):  #   Se x for string (Nome e CPF (VARCHAR(100) e CHAR(8))):
                valores.append(x)

        lista.append(valores)

    return lista



def lista_funcionarios():

    cursor.execute('SELECT * FROM Funcionario;')
    retorno = cursor.fetchall()
    lista = ['Nenhum']
    for tupla in retorno:
        valores = []
        for x in tupla:
            valores.append(x)

        lista.append(valores)

    return lista



def adicionar_veiculo(placa, cor, modelo, CPF_Cliente, CPF_Funcionario): #  Sempre retorne um argumento de CPF como None


    if CPF_Funcionario == None:

        try:
            cursor.execute('INSERT INTO Veiculo(Placa, Cor, Modelo, CPF_Cliente) VALUES(%s, %s, %s, %s);', (placa, cor, modelo, CPF_Cliente))
            conexao.commit()
            return True
        except Exception as e:
            print('Erro!', e)
            return False
        
    if CPF_Cliente == None:
        try:
            cursor.execute('INSERT INTO Veiculo(Placa, Cor, Modelo, CPF_Funcionario) VALUES(%s, %s, %s, %s);', (placa, cor, modelo, CPF_Funcionario))
            conexao.commit()
            return True
        except Exception as e:
            print('Erro!', e)
            return False
        


def adicionar_funcionario(cpf, funcao, nome):

    try:
        cursor.execute('INSERT INTO Funcionario(CPF, Funcao, Nome) VALUES(%s, %s, %s);', (cpf, funcao, nome))
        conexao.commit()
        return True
    except Exception as e:
        print('Erro!', e)
        return False
    




def listar_vagas():

    cursor.execute('SELECT Bloco, Numero FROM Vaga;')
    retorno = cursor.fetchall()
    lista = []
    for tupla in retorno:
        valores = []
        for valor in tupla:
            valores.append(str(valor))
        lista.append(valores)

    return lista





def listar_veiculos():

    cursor.execute('SELECT Placa, Modelo FROM Veiculo;')
    retorno = cursor.fetchall()
    lista = ["Nenhum"]
    for tupla in retorno:
        valores = []
        for valor in tupla:

            try:
                int(valor[-1])
            valores.append(valor)
        lista.append(valores)

    return lista





def alocar_vaga(data_entrada, hora_entrada, bloco_vaga, numero_vaga, placa_veiculo):

    try:
        cursor.execute('INSERT INTO Alocacoes(Data_Entrada, Hora_Entrada, bloco_vaga, numero_vaga, placa_veiculo) VALUES(%s, %s, %s, %s, %s)', (data_entrada, hora_entrada, bloco_vaga, numero_vaga, placa_veiculo))
        conexao.commit()
        return True
    except Exception as e:
        print('Erro!', e)
        return False