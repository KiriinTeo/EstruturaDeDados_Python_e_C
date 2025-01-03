class Node:
    def __init__(self, newItem):    # Um nó contém um item e referências para o próximo e anterior nó.
        self.item = newItem
        self.next = None
        self.prev = None

class DoubleLinkedCircularList:
    def __init__(self):             # Inicialmente, a lista está vazia, portanto `inicio` é None.
        self.inicio = None
        self.count = 0

    def IsEmpty(self):              # Verifica se a lista está vazia
        return self.inicio is None

    def InsertBefore(self, aux, newNode):   # Insere o nó `newNode` antes do nó `aux`.
        newNode.prev = aux.prev
        newNode.next = aux
        aux.prev.next = newNode
        aux.prev = newNode

    def AddFirst(self, newItem):     # Adiciona um novo item no início da lista.
        newNode = Node(newItem)
        if self.IsEmpty():           # Se a lista estiver vazia, o nó se conecta a ele mesmo.
            newNode.prev = newNode
            newNode.next = newNode
            self.inicio = newNode
        else:                        # Caso contrário, o nó é inserido antes do atual primeiro nó.
            self.InsertBefore(self.inicio, newNode)
            self.inicio = newNode

        self.count += 1

    def AddLast(self, newItem):      # Adiciona um novo item no final da lista.
        newNode = Node(newItem)
        if self.IsEmpty():
            newNode.prev = newNode
            newNode.next = newNode
            self.inicio = newNode
        else:                        # Insere o novo nó antes do nó inicial, tornando-o o último.    
            self.InsertBefore(self.inicio, newNode)
        self.count += 1

    def RemoveNode(self, aux):       # Remove o nó `aux` da lista.
        if self.count <= 1:
            self.inicio = None
        else:
            aux.prev.next = aux.next
            aux.next.prev = aux.prev

    def RemoveFirst(self):           # Remove o primeiro nó da lista.
        if self.IsEmpty():
            raise Exception("Lista vazia")
        if self.count == 1:
            self.inicio = None
        else:
            self.RemoveNode(self.inicio)
            self.inicio = self.inicio.next
        self.count -= 1

    def RemoveLast(self):            # Remove o último nó da lista.
        if self.IsEmpty():
            raise Exception("Lista vazia")
        if self.count == 1:
            self.inicio = None
        else:                        # O nó anterior ao início é o último.
            self.RemoveNode(self.inicio.prev)
        self.count -= 1

    def Remove(self, item):          # Remove o nó que contém o item especificado.
        if self.IsEmpty():
            raise Exception("Lista vazia")

        aux = self.inicio
        ult = self.inicio.prev       # Último nó
        while aux != ult and aux.item != item:
            aux = aux.next

        if aux.item != item:
            return False

        if self.count == 1:
            self.inicio = None
        else:
            self.RemoveNode(aux)
            if aux == self.inicio:
                self.inicio = self.inicio.next
        self.count -= 1
        return True

    def PrintList(self):              # Exibe todos os itens da lista circular duplamente encadeada.
        if self.IsEmpty():
            print("Lista vazia")
            return
        
        aux = self.inicio
        while True:
            print(aux.item, end=" <-> ")
            aux = aux.next
            if aux == self.inicio:
                break
        print()
        
def menu():
    DoubleList = DoubleLinkedCircularList()
    
    while True:
        print("\n1 - Adicionar no inicio")
        print("2 - Adicionar no fim")
        print("3 - Remover do inicio")
        print("4 - Remover do fim")
        print("5 - Remover elemento espeficifico")
        print("6 - Imprimir a lista")
        print("7 - Remover Node da lista (não faz nada)") 
        print("8 - Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            valor = input("Digite algo para adicionar no incio: ")
            DoubleList.AddFirst(valor)
        elif opcao == 2:
            valor = int(input("Digite um número para adicionar no fim: "))
            DoubleList.AddLast(valor)
        elif opcao == 3:
            try:
                DoubleList.RemoveFirst()
                print("Elemento removido do inicio.")
            except Exception as e:
                print(e)
        elif opcao == 4:
            try: 
                DoubleList.RemoveLast()
                print("Elemento removido do fim.")
            except Exception as e:
                print(e)
        elif opcao == 5:
            valor = int(input("Digite o valor do elemento a ser removido: "))
            if DoubleList.Remove(valor):
                print(f"Elemento {valor} removido.")
            else:
                print(f"Elemento {valor} não encontrado.")
        elif opcao == 6:
            DoubleList.PrintList()
        elif opcao == 8:
            break
        else:
            print("Opção inválida. Tente novemente.")
            
menu()

# Exemplo de uso: Amplificar a Eficiência de busca da lista.
# Loop do menu para o usuário