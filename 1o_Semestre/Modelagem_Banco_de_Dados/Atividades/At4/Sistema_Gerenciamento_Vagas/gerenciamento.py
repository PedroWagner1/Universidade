import customtkinter as ctk
import db



#   JANELA DE CLIENTE:

def add_cliente():

    janela_cliente = ctk.CTk()
    janela_cliente.geometry('800x600')
    janela_cliente.minsize(width=800, height=600)
    janela_cliente.maxsize(width=800, height=600)
    janela_cliente.title('Gerenciamento')


    #   Nome Cliente:

    txt_nome = ctk.CTkEntry(janela_cliente, placeholder_text='Insira o Nome do Cliente', width=280, height=30)
    txt_nome.pack(pady=(30, 10))

    #   CPF Cliente:

    txt_cpf = ctk.CTkEntry(janela_cliente, placeholder_text='Insira o CPF do cliente, Formato: 00000000000', width=280, height=30)
    txt_cpf.pack(pady=(30, 10))

    #   Gestante:

    lbl_gestante = ctk.CTkLabel(janela_cliente, text='Gestante?')
    lbl_gestante.pack(pady=(30, 5))

    box_gestante = ctk.CTkComboBox(janela_cliente, values=['sim', 'nao'])
    box_gestante.pack()


    #   Deficiente:

    lbl_deficiente = ctk.CTkLabel(janela_cliente, text='Deficiente?')
    lbl_deficiente.pack(pady=(30, 5))

    box_deficiente = ctk.CTkComboBox(janela_cliente, values=['sim', 'não'])
    box_deficiente.pack(pady=(30,15))


    #   Data_Nascimento

    txt_data_nasc = ctk.CTkEntry(janela_cliente, placeholder_text='Data de Nascinmento. Formato: YYYY-MM-DD', width=330)
    txt_data_nasc.pack(pady=(10,20))


#   Cliente Adicionado! ou Não Adicionado!

    txt_cliente_adicionado = ctk.CTkLabel(janela_cliente, text='')
    txt_cliente_adicionado.pack(pady=(10, 10))

    #   Botão Adicionar Cliente:
    #   Adiciona os valores ao banco de dados:
    btn_adicionarcliente = ctk.CTkButton(janela_cliente, text='Adicionar Cliente', height=50, command=lambda: txt_cliente_adicionado.configure(text='Cliente Adicionado!') if db.adicionar_cliente(txt_cpf.get(), txt_nome.get(), txt_data_nasc.get(), 1 if box_gestante.get() == 'sim' else 0, 1 if box_deficiente.get() == 'sim' else 0) else txt_cliente_adicionado.configure(text='Ocorreu um Erro! Revise os dados e tente novamente'))
    btn_adicionarcliente.pack()


    janela_cliente.mainloop()






#   JANELA DO VEÍCULO:

def add_veiculo():


        #   Configurações da janela:

    janela_veiculo = ctk.CTk()
    janela_veiculo.geometry('800x600')
    janela_veiculo.minsize(width=800, height=600)
    janela_veiculo.maxsize(width=800, height=600)
    janela_veiculo.title('Gerenciamento')


    #   Placa:

    txt_placa = ctk.CTkEntry(janela_veiculo, placeholder_text='Placa do Veículo. Formato: XXX000 ou XXX0X00', width=500)
    txt_placa.pack(pady=(30,20))


    #   Cor:
    txt_cor = ctk.CTkEntry(janela_veiculo, placeholder_text='Cor do Veículo', width=500)
    txt_cor.pack(pady=(10, 20))

    #   Modelo:
    txt_modelo = ctk.CTkEntry(janela_veiculo, placeholder_text='Modelo do Veículo', width=500)
    txt_modelo.pack(pady=(10,20))

    #   CPF_Cliente:

    lbl_aviso = ctk.CTkLabel(janela_veiculo, text='Aviso: Você somente pode implementar Funcionário OU Cliente.')
    lbl_aviso.pack()

    lbl_cliente = ctk.CTkLabel(janela_veiculo, text='Cliente:')
    lbl_cliente.pack(pady=(10, 10))
    box_cpfcliente = ctk.CTkComboBox(janela_veiculo, values=[" ".join(x) for x in db.lista_clientes()])
    box_cpfcliente.pack(pady=(10,30))


    #   CPF_Funcionario:

    lbl_funcionario = ctk.CTkLabel(janela_veiculo, text='Funcionario:')
    lbl_funcionario.pack(pady=(10, 10))
    box_cpffuncionario = ctk.CTkComboBox(janela_veiculo, values=[" ".join(x) for x in db.lista_funcionarios()])
    box_cpffuncionario.pack()



    lbl_erro = ctk.CTkLabel(janela_veiculo, text='')
    lbl_erro.pack()

    #   Botão Atribuir:

    btn_atribuir = ctk.CTkButton(janela_veiculo, text='Adicionar Veículo', command=lambda:lbl_erro.configure(text='Veículo Adicionado com Sucesso') if db.adicionar_veiculo(txt_placa.get(), txt_cor.get(), txt_modelo.get(), None if box_cpfcliente.get() == 'N e n h u m' else box_cpfcliente.get().split(' ')[0], None if box_cpffuncionario.get() == 'N e n h u m' else box_cpffuncionario.get().split(' ')[0]) else lbl_erro.configure(text='Erro ao adicionar! Revise os dados'))
    btn_atribuir.pack(pady=(10, 30))

 


    janela_veiculo.mainloop()






def add_funcionario():

    janela_funcionario = ctk.CTk()
    janela_funcionario.geometry('800x600')
    janela_funcionario.minsize(width=800, height=600)
    janela_funcionario.maxsize(width=800, height=600)
    janela_funcionario.title('Gerenciamento')






    #   CPF:    

    txt_cpf = ctk.CTkEntry(janela_funcionario, placeholder_text='Insira o CPF. Formato: 12312312399', width=500, height=40)
    txt_cpf.pack(pady=(20,15))

    #   Nome:
    txt_nome = ctk.CTkEntry(janela_funcionario, placeholder_text='Insira o Nome', width=500, height=40)
    txt_nome.pack(pady=(20, 15))

    #   Função:
    txt_funcao = ctk.CTkEntry(janela_funcionario, placeholder_text='Insira a Função', width=500, height=40)
    txt_funcao.pack(pady=(20,15))


    #   Label de retorno:

    lbl_status = ctk.CTkLabel(janela_funcionario, text='')
    lbl_status.pack(pady=(10, 15))

    #   Botão de atribuir:

    btn_atribuir = ctk.CTkButton(janela_funcionario, text='Adicionar Funcionário', command=lambda: lbl_status.configure(text='Funcionário Inserido com Sucesso!') if db.adicionar_funcionario(txt_cpf.get(), txt_funcao.get(), txt_nome.get()) else lbl_status.configure(text='Ocorreu um erro! Verifique os dados'))
    btn_atribuir.pack(pady=(10, 15))



    janela_funcionario.mainloop()







def alocar_vaga():


    janela_alocacao = ctk.CTk()
    janela_alocacao.geometry('800x600')
    janela_alocacao.minsize(width=800, height=600)
    janela_alocacao.maxsize(width=800, height=600)
    janela_alocacao.title('Gerenciamento')



    #   DATA ENTRADA:

    txt_data = ctk.CTkEntry(janela_alocacao, placeholder_text='Insira a data de Entrada. Formato: YYYY-MM-DD', height=40, width=500)
    txt_data.pack(pady=(20, 15))


    #   HORA ENTRADA:

    txt_hora = ctk.CTkEntry(janela_alocacao, placeholder_text='Insira o horário de entrada. Formato: HH:MM:SS', height=40, width=500)
    txt_hora.pack(pady=(10, 15))


    #   Vaga:
    lbl_vaga = ctk.CTkLabel(janela_alocacao, text='Escolha a vaga:')
    lbl_vaga.pack(pady=(10, 15))
    box_vagas = ctk.CTkComboBox(janela_alocacao, values=["".join(x) for x in db.listar_vagas()])
    box_vagas.pack(pady=(10,15))


    #   Veículo:

    lbl_veiculo = ctk.CTkLabel(janela_alocacao, text='Escolha o Veículo:')
    lbl_veiculo.pack(pady=(10, 15))

    box_veiculo = ctk.CTkComboBox(janela_alocacao, values=["".join(x) for x in db.listar_veiculos()])
    box_veiculo.pack(pady=(10, 15))


    #   Estado:

    lbl_estado = ctk.CTkLabel(janela_alocacao, text='')
    lbl_estado.pack(pady=(10, 15))


    #   aTRIBUIR:

    #btn_atribuir = ctk.CTkButton(janela_alocacao, text='Alocar Vaga', command=lambda: lbl_estado.configure(text='Vaga Alocada!') if db.alocar_vaga(txt_data.get(), txt_hora.get(), box_vagas.get()[0], box_vagas.get()[1:2], box_veiculo))
    #btn_atribuir.pack(pady=(10,15))


    janela_alocacao.mainloop()












#   configurações gerais da janela:
janela = ctk.CTk()
janela.geometry('800x600')
janela.minsize(width=800, height=600)
janela.maxsize(width=800, height=600)
janela.title('Gerenciamento')


#   Botão Adicionar Cliente:
btn_add_cliente = ctk.CTkButton(janela, text='Adicionar Cliente', height=50, command=add_cliente)
btn_add_cliente.pack(pady=(30, 10))

#   Botão Adicionar Veículo
btn_add_veiculo = ctk.CTkButton(janela, text='Adicionar Veículo', height=50, command=add_veiculo)
btn_add_veiculo.pack(pady=(30, 10))

#   Botão Adicionar Funcionário
btn_add_funcionario = ctk.CTkButton(janela, text='Adicionar Funcionário', height=50, command=add_funcionario)
btn_add_funcionario.pack(pady=(30, 10))

#   Botão Alocar Vaga
btn_add_alocacao = ctk.CTkButton(janela, text='Alocar uma Vaga', height=50, command=alocar_vaga)
btn_add_alocacao.pack(pady=(30,10))

janela.mainloop()