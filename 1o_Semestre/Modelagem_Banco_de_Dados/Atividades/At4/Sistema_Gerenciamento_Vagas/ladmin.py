#   Script simples para alterar o Json de admin 


import json

login = {'user': 'admin',
         'password': 'adminp@ssw'
         }


with open('login_admin.json', 'w', encoding='utf8') as l:
    json.dump(login, l)