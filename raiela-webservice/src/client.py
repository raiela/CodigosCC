import requests

api_url = 'http://localhost:5000'

while True:
    print("\n\nEscolha uma opção: (0 - sair)")
    print("1 - Listar Casters")
    print("2 - Listar Caster por ID")
    print("3 - Adicionar Caster")
    print("4 - Alterar Caster")
    print("5 - Remover Caster")
    
    opc = input()
    
    if opc == "0":
        break
    
    elif opc == "1":

        response = requests.get(api_url+"/casters")
        print("\n\nCasters:")
        print("------------ *** ------------\n")
        for caster in response.json()['casters']:
            print("ID: " + caster['id'])
            print("Nome: " + caster['nome'])
            print("Disponibilidade: " + caster['disponibilidade'])
            print('...............................')
        print("\n------------ *** ------------\n")
        
    elif opc == "2":
        id = input("Digite o ID: ")
        response = requests.get(api_url+"/casters/"+id)
        if "error" in response.json(): 
            print("ID inválido")
        else:
            caster = response.json()['caster']
            print("------------ *** ------------\n")
            print("ID: " + caster['id'])
            print("Nome: " + caster['nome'])
            print("Disponibilidade: " + caster['disponibilidade'])

    elif opc == "3":
        nome = input("Digite o nome do caster: ")
        disponibilidade = ""
        while True:
            d = input("Disponibilidade: (ou a palavra sair) ")
            if(d == 'sair'):
                break
            disponibilidade += d+'-'
        
        caster = {
            "nome": nome,
            "disponibilidade": disponibilidade,
        }
        response = requests.post(api_url+"/casters", json=caster)
        caster_created = response.json()['caster']
        print("Produto criado!")
        
    elif opc == "4":
        id = input("Digite o ID do caster que deseja alterar: ")
        nome = input("Digite o nome: ")
        disponibilidade = ""
        while True:
            d = input("Disponibilidade: (ou sair)")
            if(d == 'sair'):
                break
            disponibilidade += d+'-'
            
        caster = {
            "nome": nome,
            "disponibilidae": disponibilidade,
        }
        response = requests.put(api_url+"/casters/"+id, json=caster)
        if "error" in response.json(): 
            print("ID inválido")
        else:
            caster_created = response.json()['caster']
            print("Produto criado!")
            
    elif opc == "5":
        id = input("Digite o ID caster: ")
        response = requests.delete(api_url+"/casters/"+id)
        if "error" in response.json(): 
            print("ID inválido")
        else:
            result = response.json()['result']
            if result == True:
                print("O caster foi deletado com sucesso\n")
            else: 
                print("Não foi possível deletar o produto")

    else:
        print("Opção inválida")