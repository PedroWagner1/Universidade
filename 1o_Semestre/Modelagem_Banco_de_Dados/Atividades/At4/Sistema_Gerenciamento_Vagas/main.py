import customtkinter as ctk
import json

#   Função para verificar login que é passada em button:

def verificar_login():
    
    #   Guard Clause para encerrar caso valores sejam vazios

    if not txt_user.get() or not txt_pass.get():
        lbl_erro_sem_valor.configure(text='Os valores não podem estar vazios!')
        return

    lbl_erro_sem_valor.configure(text='')

    with open('login_admin.json', 'r', encoding='utf8') as login:
        infos = json.load(login)


        #   Condicional que verifica se valores são iguais às credenciais de admin:
        if txt_user.get() == infos['user'] and txt_pass.get() == infos['password']:
            
            janela.destroy()
            import gerenciamento as gerenciamento   #   Importa a janela de gerenciamento
            

        else:
            lbl_erro_sem_valor.configure(text='Credenciais inválidas!')









ctk.set_appearance_mode('Dark')

janela = ctk.CTk()  #   janela principal

janela.geometry("780x520")  #   define o tamanho da janela
janela.title('Gerenciamento de Vagas')

#   ambas as configurações tornam a janela não redimensionável
janela.minsize(width=780, height=520)
janela.maxsize(width=780, height=520)


    #   Texto inicial:
lbl_inicial = ctk.CTkLabel(janela, text='Sistema de Gerenciamento de Vagas em Estacionamento Privado', font=('FreeMono', 17), text_color='white')
lbl_inicial.pack(pady=10, padx=20)


#   Título Login:
lbl_login = ctk.CTkLabel(janela, text='Login:', font=('FreeMono', 22))
lbl_login.pack(pady=(30, 15))


#   Label para o input de usuário
lbl_user = ctk.CTkLabel(janela, text='usuario:', font=('FreeMono', 19))
lbl_user.pack(padx=40, pady=10, anchor='w')


#   Input de User 
txt_user = ctk.CTkEntry(janela, placeholder_text='Insira o usuário de administrador', width=280, height=30)
txt_user.pack(anchor='w', padx=60, pady=(10, 30))



#   Label para o input de senha:

lbl_pass = ctk.CTkLabel(janela, text='Senha:', font=('FreeMono', 19))
lbl_pass.pack(padx=40, pady=10, anchor='w')

#   Input da senha:
txt_pass = ctk.CTkEntry(janela, placeholder_text='Insira a senha de Administrador:', width=280, height=30, show='*')
txt_pass.pack(anchor='w', padx=60)



#   Botão de Login:

btn_login = ctk.CTkButton(janela, text='Login', height=45, command=verificar_login)
btn_login.pack(pady=(80, 10))


 #   Executa verificar_login para os valores de


# 1a Mensagem de erro:
lbl_erro_sem_valor = ctk.CTkLabel(janela, text='', text_color='red')
lbl_erro_sem_valor.pack(pady=5)



janela.mainloop()