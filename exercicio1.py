# Feito por Daniel Gama - RU:4121047
class Nodo:  # Criando Classe Nodo
    def __init__(self, numero, cor):  # Método Construtor
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:  # Criando Classe ListaEncadeada
    def __init__(self):  # Método Construtor
        self.head = None

    def inserirSemPrioridade(self, nodo):  # Função para inserir sem prioridade
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):  # Função para inserir com prioridade
        if self.head is None:
            self.head = nodo
        elif self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):  # Função para inserir, encaminha para com/sem prioridade
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        numero = int(input("Digite o número do cartão: "))
        nodo = Nodo(numero, cor)

        if self.head is None:
            self.head = nodo
        elif cor == "V":
            self.inserirSemPrioridade(nodo)
        elif cor == "A":
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(
        self,
    ):  # Função para imprimir a lista de espera ou mostrar que está vazia
        if self.head is None:
            print("A lista de espera está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(f"Cartão {atual.cor} número {atual.numero}")
                atual = atual.proximo

    def atenderPaciente(
        self,
    ):  # Função para chamar o paciente ou mostrar que não há mais pacientes
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            print(
                f"Chamando paciente com cartão {self.head.cor} número {self.head.numero}"
            )
            self.head = self.head.proximo


def menu():  # Função do menu principal
    lista = ListaEncadeada()
    while True:
        print()
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print()
            lista.inserir()
        elif opcao == 2:
            print()
            lista.imprimirListaEspera()
        elif opcao == 3:
            print()
            lista.atenderPaciente()
        elif opcao == 4:
            print()
            print("Encerrando o programa.")
            break
        else:
            print()
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    print("\n-- Programa Triagem Hospital // Daniel Gama RU: 4121047  --")
    print()
    menu()
