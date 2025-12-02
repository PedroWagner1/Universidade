import pymysql

conexao = pymysql.connect(host='127.0.0.1', user='root', password='P@ssFlow', database='sistema_gerenciamento')
cursor = conexao.cursor()

blocos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

for bloco in blocos:    #   Itera sobre cada bloco

    for numero in range(1, 31): #   Itera sobre 30 numeros para cada bloco
        
        cursor.execute('INSERT INTO Vaga(Bloco, Numero, Estado) VALUES(%s, %s, 0)', (bloco, numero))
        conexao.commit()