class Contato:
    def __init__(self):
        self.nome = None
        self.email = None
        self.telefone = None

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_email(self):
        return self.email

    def set_email(self, novo_email):
        self.email = novo_email

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone


class Agenda:
    def __init__(self):
        self.agenda = []  # Lista para guardar os contatos.

    def get_agenda(self):
        return self.agenda

    def set_agenda(self, nova_agenda):
        self.agenda = nova_agenda

    def incluir_contato(self):
        print()
        nome = str(input('Nome completo: ')).strip()
        email = str(input('Email: ')).strip()
        telefone = str(input('Telefone: ')).strip()
        print('Contato adicionado com sucesso!\n')

        contato = Contato()
        contato.set_nome(nome)
        contato.set_email(email)
        contato.set_telefone(telefone)

        self.get_agenda().append(contato)  # Guardando o contato na agenda.

    def listar_contatos(self):
        print()
        if self.get_agenda() == []:  # Lista vazia.
            print('Não há contatos cadastrados na agenda.')
        else:
            for index, contato in enumerate(self.get_agenda()):
                print('-' * 30)
                print(f'Contato {index + 1}:')
                print(f'Nome completo: {contato.get_nome()}')
                print(f'Email: {contato.get_email()}')
                print(f'Telefone: {contato.get_telefone()}')
                print('-' * 30)
        print()

    def buscar_contato(self):
        print()
        if self.get_agenda() == []:
            print('Não há contatos cadastrados na agenda.')
        else:
            termo = str(input('Digite o termo que você deseja buscar: ')).strip()
            for index, contato in enumerate(self.get_agenda()):
                if(contato.get_nome().find(termo) + contato.get_email().find(termo) + contato.get_telefone().find(termo)) >= -2:  # O find retorna -1 se o termo não for encontrado.
                    print('-' * 30)
                    print(f'Contato {index + 1}:')
                    print(f'Nome: {contato.get_nome()}')
                    print(f'Email: {contato.get_email()}')
                    print(f'Telefone: {contato.get_telefone()}')
                    print('-' * 30)
                else:
                    print('Nenhum contato encontrado. Tente novamente.')
        print()

    def editar_contato(self):
        print()
        if self.get_agenda() == []:
            print('Não há contatos cadastrados na agenda.\n')
        else:
            self.listar_contatos()
            id = int(input('Digite o id do contato que você deseja editar: '))
            
            # É usado [id - 1] devido ao id do contato ser mostrado com o incremento de 1 em def listar_contato().
            novo_nome = str(input(f'Novo nome para {self.get_agenda()[id - 1].get_nome()}: ')).strip()
            if novo_nome != '':
                self.get_agenda()[id - 1].set_nome(novo_nome)

            novo_email = str(input(f'Novo email para {self.get_agenda()[id - 1].get_email()}: ')).strip()
            if novo_email != '':
                self.get_agenda()[id - 1].set_email(novo_email)

            novo_telefone = str(input(f'Novo telefone para {self.get_agenda()[id - 1].get_telefone()}: ')).strip()
            if novo_telefone != '':
                self.get_agenda()[id - 1].set_telefone(novo_telefone)
            
            print('Dados alterados com sucesso!\n')

    def excluir_contato(self):
        print()
        if self.get_agenda() == []:
            print('Não há contatos cadastrados na agenda.\n')
        else:
            self.listar_contatos()
            id = int(input('Digite o id do contato que você deseja excluir: '))
            del self.get_agenda()[id - 1]
            print('Contato excluído com sucesso!\n')


class Menu:
    def __init__(self):
        self.opcao = None

    def get_opcao(self):
        return self.opcao

    def set_opcao(self, nova_opcao):
        self.opcao = nova_opcao

    def executar(self):
        agenda = Agenda()

        while self.get_opcao() != '6':
            print('-' * 30)
            print('            MENU')
            print('-' * 30)
            print('[1] - Adicionar contato')
            print('[2] - Buscar contato')
            print('[3] - Editar contato')
            print('[4] - Excluir contato')
            print('[5] - Listar contatos')
            print('[6] - Sair')

            opcao = str(input('Digite a opção desejada: '))
            self.set_opcao(opcao)

            if self.get_opcao() == '1':
                agenda.incluir_contato()
            elif self.get_opcao() == '2':
                agenda.buscar_contato()
            elif self.get_opcao() == '3':
                agenda.editar_contato()
            elif self.get_opcao() == '4':
                agenda.excluir_contato()
            elif self.get_opcao() == '5':
                agenda.listar_contatos()
            elif self.get_opcao() == '6':
                print('Até mais.')
            else:
                print('\nOpção inválida! Tente novamente.\n')


# Execução
menu = Menu()
menu.executar()
