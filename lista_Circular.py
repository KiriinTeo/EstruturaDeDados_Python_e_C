class Node:
    def __init__(self, newItem, nextNode=None):  # Define um nó com um valor e um ponteiro para o próximo.
        self.item = newItem
        self.next = nextNode

class CircularLinkedList:
    def __init__(self):  # Inicializa a lista circular vazia.
        self.final = None
        self.count = 0

    def IsEmpty(self):  # Verifica se a lista está vazia.
        return self.final is None

    def AddFirst(self, newItem):  # Adiciona um elemento no início da lista.
        newNode = Node(newItem)
        if not self.IsEmpty():
            newNode.next = self.final.next
            self.final.next = newNode
        else:
            newNode.next = newNode
            self.final = newNode
        self.count += 1

    def AddLast(self, newItem):  # Adiciona um elemento no final da lista.
        self.AddFirst(newItem)
        self.final = self.final.next

    def RemoveFirst(self):  # Remove o primeiro elemento da lista, verificando se ela está vazia.
        if self.IsEmpty():
            raise Exception("Lista vazia")
        if self.count == 1:
            self.final = None
        else:
            self.final.next = self.final.next.next
        self.count -= 1

    def RemoveLast(self):  # Remove o último elemento da lista, verificando se ela está vazia.
        if self.IsEmpty():
            raise Exception("Lista vazia")
        if self.count == 1:
            self.final = None
        else:
            aux = self.final.next
            while aux.next != self.final:
                aux = aux.next
            aux.next = self.final.next
            self.final = aux
        self.count -= 1

    def Remove(self, item):  # Remove um elemento específico da lista.
        if self.IsEmpty():
            raise Exception("Lista vazia")
        aux = self.final.next
        anterior = self.final

        while aux != self.final and aux.item != item:
            anterior = aux
            aux = aux.next

        if aux.item != item:
            return False

        if aux == aux.next:
            self.final = None
        else:
            anterior.next = aux.next
            if aux == self.final:
                self.final = anterior

        self.count -= 1
        return True

    def PrintList(self):  # Imprime todos os elementos da lista.
        if self.IsEmpty():
            print("Lista vazia")
            return
        aux = self.final.next
        while True:
            print(aux.item, end=" -> ")
            aux = aux.next
            if aux == self.final.next:
                break
        print()

def main():  # Exibe um menu interativo para manipular a lista circular.
    circularList = CircularLinkedList()
    circularList.AddLast(10)
    circularList.AddLast(20)
    circularList.AddLast(30)

    while True:
        print("\n1 - Adicionar no inicio")
        print("2 - Adicionar no fim")
        print("3 - Remover do inicio")
        print("4 - Remover do fim")
        print("5 - Remover elemento especifico")
        print("6 - Imprimir a lista")
        print("7 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor = int(input("Digite um número para adicionar no inicio: "))
            circularList.AddFirst(valor)
        elif opcao == 2:
            valor = int(input("Digite um número para adicionar no fim: "))
            circularList.AddLast(valor)
        elif opcao == 3:
            try:
                circularList.RemoveFirst()
                print("Elemento removido do inicio.")
            except Exception as e:
                print(e)
        elif opcao == 4:
            try:
                circularList.RemoveLast()
                print("Elemento removido do fim.")
            except Exception as e:
                print(e)
        elif opcao == 5:
            valor = int(input("Digite o valor do elemento a ser removido: "))
            if circularList.Remove(valor):
                print(f"Elemento {valor} removido.")
            else:
                print(f"Elemento {valor} não encontrado.")
        elif opcao == 6:
            circularList.PrintList()
        elif opcao == 7:
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
