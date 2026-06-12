import json
import os
from datetime import datetime



def next_id(contacts):              #gerar prÃ³ximo ID 
    if not contacts:
        return 1
    return max(contact['id'] for contact in contacts) + 1


def register_contact(contacts):  
    contacts_id = next_id(contacts)           #registrar um contato novo
    name = input("Nome do Contato: ").strip()
    surname = input("Sobrenome do Contato: ").strip()
    number_contact = input("Numero do Contato: ").strip()
    description = input("Descricao do contato: ").strip()
    new_contact = {
        'id' : contacts_id,
        'name' : name,
        'surname' : surname,
        'number_contact' : number_contact,
        'description' : description,
        'date': datetime.now().strftime("%Y-%m-%d %H %M %S")
    }
    contacts.append (new_contact)
    print(f" O Contato do {name} foi cadastrado com sucesso com o ID {contacts_id}.")


def list_contacts(contacts):
    if not contacts:
        print("Nenhum contato cadastrado! ")
        return
    print("ID | Name | Surname | Number Contact | Description | Date")
    print("---------------------------------------------------")
    for contact in contacts :
        print(f"{contact ['id']} | {contact ['name']} | {contact ['surname']} | {contact['number_contact']} | {contact['description']} | {contact['date']}")



def search_contact(contacts):
    search_contact = input("Informe o Nome do contato que vc deseja buscar: ").lower()
    found_contact = [c for c in contacts if search_contact in c ['name'].lower()]
    if not found_contact:
        print("Nenhum contato Encontrado")
        return  
    print("ID | Name | Surname | Number Contact | Description | Date")
    print("---------------------------------------------------")
    for contact in found_contact:
        print(f"{contact ['id']} | {contact ['name']} | {contact ['surname']} | {contact['number_contact']} | {contact['description']} | {contact['date']}")      

def qtd_contacts(contacts):
    count = 0
    for c in contacts:
        count += 1
    print (f"Atualmente o número total de contatos é {count}")
    if not contacts:
        print("Atualmente nÃ£o possui nenhum contato cadastrado")

def remove_contact(contacts):
    nome = input("Informe o contato que vc deseja remover: ").strip()

    for contact in contacts:
        if  (contact['name'].strip().lower() == nome.lower()):
            contacts.remove(contact)
            print(f"O Contato {nome} foi removido com sucesso! ")
            return
        
    print("Nenhum contato encontrado !")

def edit_contact (contacts):
    name = input("Informe o Contato que vc deseja editar").strip()

    for contact in contacts:
        if (contact['name'].strip().lower() == name.lower()):
            contact['name'] = input(new_name)


    print("Nenhum contato Encontrado, verifique os contatos cadastrados! ")