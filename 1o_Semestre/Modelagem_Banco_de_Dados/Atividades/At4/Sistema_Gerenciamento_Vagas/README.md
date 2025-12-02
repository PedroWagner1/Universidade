#   Sistema de Gerenciamento de Vagas em Estacionamento

Este é um projeto que implementa efetivamente, não só a aplicação dos comandos SQL para transformar o modelo lógico em uma aplicação real, mas também implementa a nível de conceito um programa GUI para interação com usuário através da linguagem Python e da biblioteca Tkinter. Neste caso, para maior elegância visual estarei utilizando o customtkinter, o SGBD utilizado será o Mysql e a biblioteca que irei usar para integrar o SGBD com o programa será o pymysql.


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