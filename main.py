import contact
from files import load_json,save_json

contacts = load_json('contacts.json') or []




while True:
    
    print("==>> Agenda de Contatos <<==")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contatos")
    print("4 - Remover contatos")
    print("5 - Esitar Contatos")
    print("6 - Quantidade de contatos")
    print("7 - Salvar e sair")

    op = int(input("Informe a opção desejada: "))
    match op:
        case 1:
            contact.register_contact(contacts)
        case 2:
            contact.list_contacts(contacts)
        case 3:
            contact.search_contact(contacts)
        case 4:
            contact.remove_contact(contacts)
        case 5:
            contact.edit_contact(contacts)
        case 6:
            contact.qtd_contacts(contacts)
        case 7:
            save_json(contacts,'contacts.json')
            print("Salvando os Dados...\n Encerrando o Sistema...")
            break
        case _:
            print("Opção Inválida, verifique as opções disponivéis! ")