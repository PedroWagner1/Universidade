#   Sistema de Gerenciamento de Vagas em Estacionamento

Este é um projeto que implementa efetivamente, não só a aplicação dos comandos SQL para transformar o modelo lógico em uma aplicação real, mas também implementa a nível de conceito um programa GUI para interação com usuário através da linguagem Python e da biblioteca Tkinter. Neste caso, para maior elegância visual estarei utilizando o customtkinter, o SGBD utilizado será o Mysql e a biblioteca que irei usar para integrar o SGBD com o programa será o pymysql.

O repositório em questão apresenta um trabalho da Faculdade Referente à Banco de Dados e Linguagem SQL.

O projeto apresenta a aplicação física do modelo lógico feito nas outras atividades e sua integração com um aplicativo interativo feito co customtkinter e Python


Para uma melhor organização do código, utilizei a notação húngara (conceito que aprendi durante meus estudos de VB.NET)

Obs: O programa utiliza a fonte FreeMono (uma fonte que achei disponível no meu Linux), favor consultar se esta mesma fonte é existente em sistemas Windows.


#   Login e Senha de Administrador:

    O login e senha de administrador é definido em login_admin.json e por padrão, é:

    user: admin
    password: adminp@ssw

    Mais a nível de prova de conhecimento, criei um script bem simples ladmin.py que dumpa as credenciais de administrador para login_admin.json através
    da biblioteca json, usando o método .dump() e um context manager para gerenciar o conteúdo do arquivo corretamente.


    no arquivo main.py, temos uma função denominada verificar_login, que primeiramente possui um Guard Clause para o caso de os valores do input de usuário ou senha estiverem vazios, e depois possui uma condicional que verificar se os valores destes input's correspondem com os valores da chave ['user'] e ['password'] do json login_admin.json (carregado via json.load)



#   Considerações:

    A proposta oficial do sistema é ser um sistema sem muita interação digital no que diz respeito ao registro de veículos (que é feito através de uma câmera OCR), atribuição destes veículos aos clientes, atribuição de vagas, etc. Sendo um sistema focado na integridade, efetividade e automação total. Ainda assim, não seria possível demonstrar estes conceitos na prática sem os equipamentos nescessários para isto, considerando este fato, todos os casos de uso estarão incluídos para registro direto no banco de dados através da janela de gerenciamento que é passada após a verificação de login ser sucedida.



#   Sobre o Banco de Dados e o SGBD

    O SGBD utilizado é mysql-server, é imprescendível que, para rodar o programa corretamente, antes deva-se configurar:

    1. 
   <code> conexao = pymysql.connect(host='127.0.0.1', user='root', password='rootp@ssw', database='sistema') </code>
     Para os argumentos corretos

    2.
    Todos os comandos sql existentes no arquivo estrutura_bd.sql   
        (um exemplo de fazer isso seria:) <code>    mysql -u root -p < estrutura_bd.sql </code>

    3. Rodar o script criar_vagas.py uma única vez após ter rodado o arquivo .sql



#   O arquivo db.py

Este arquivo é o responsável por realizar as consultas e as alterações no Banco de Dados efetivamente através da biblioteca pymysql.

Eu fui desenvolvendo as funções de uso deste arquivo conforme eu via necessidade das implementações com o aplivativo.

A maioria das funções são chamadas quando o usuário clica em algum botão referente.


#   O arquivo gerenciamento.py

Este é o arquivo que contém todas as chamadas de consultas (do db.py) e todo o código do sistema de gerenciamento. Eu optei por definir cada subjanela da janela principal em funções neste módulo, ao invés de criar em outros módulos. A janela principal possui alguns botões, nos quais recebem um argumento command= referenciando suas respectivas funções que abrem suas janelas. Em cada janela, nós temos campos de inserção (ctk.CTkEntry(), ctk.CTkComboBox()) de dados para os dados nescessários e requerentes a cerca das operações no banco de dados. A respeito das verificações dos dados inseridos nestes campos, por ser um projeto com intuito didático e de prova de conhecimento, eu decidi não implementar estas verificações, também porque estava com pouco tempo para finalizar. AInda assim o formato de como os dados devem ser inseridos estão informados nos respectivos placeholder's de cada entrada.

Exemplo de um campo de entrada de texto na janela veiculo:

<code>  txt_placa = ctk.CTkEntry(janela_veiculo, placeholder_text='Placa do Veículo. Formato: XXX000 ou XXX0X00', width=500)
txt_placa.pack(pady=(30,20))</code>

Ao clicar no botão atribuir, o módulo chama a respectiva função do módulo db.py para aquela operação, por exemplo: adicionar_cliente.

Estas funções possuem argumentos que devem ser passados aos parâmetros da função, e, caso retorne algum erro, então:

<code>except Exception as e:
            print('Erro!', e)
            return False</code>

o sistema exibe o erro e retorna False.

        
Caso uma função de db.py retorne True, então os dados foram inseridos com suceso, caso contrário, houve algum erro. É exatamente esta condição que nós utilizamos para atualizar a label de erros ou acertos presente em cada janela.

        
<code>     btn_atribuir = ctk.CTkButton(janela_veiculo, text='Adicionar Veículo', command=lambda:lbl_erro.configure(text='Veículo Adicionado com Sucesso') if db.adicionar_veiculo(txt_placa.get(), txt_cor.get(), txt_modelo.get(), None if box_cpfcliente.get() == 'N e n h u m' else box_cpfcliente.get().split(' ')[0], None if box_cpffuncionario.get() == 'N e n h u m' else box_cpffuncionario.get().split(' ')[0]) else lbl_erro.configure(text='Erro ao adicionar! Revise os dados'))
 </code>
