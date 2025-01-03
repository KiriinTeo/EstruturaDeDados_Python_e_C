class Tarefa:
    def __init__(self, numero): # Define cada tarefa com um identificador próprio (um número) e um indicador para a próxima tarefa
        self.numero = numero                                      
        self.proximo = None                                       

class ListaDeTarefas:
    def __init__(self): # Inicia a lista sem nenhuma tarefa e quntidade zero
        self.cabeca = None                                        
        self.quantidade = 0                                       

    def adicionar_no_inicio(self, numero): # Cria uma nova tarefa e aponta ela para a "cabeça" (inicio) e incrementa a quantidade.
        nova_tarefa = Tarefa(numero)                              
        nova_tarefa.proximo = self.cabeca                         
        self.cabeca = nova_tarefa                                 
        self.quantidade += 1                                      
        print(f"Tarefa {numero} adicionada no início da lista.")  

    def adicionar_no_fim(self, numero): # Também cria nova tarefa mas percorre a lista até o final e adiciona lá # 
        nova_tarefa = Tarefa(numero)    # Incrementa a quantidade
        if self.cabeca is None:         # Caso a lista estiver vazia, aponta para a "cabeça"
            self.cabeca = nova_tarefa                              
        else:
            atual = self.cabeca                                    
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nova_tarefa                            
        
        self.quantidade += 1                                       
        print(f"Tarefa {numero} adicionada no fim da lista.")

    def remover_tarefa(self, numero): # Busca a tarefa percorrendo a lista 
        atual = self.cabeca           # Quando encontrada, caso for a "cabeça" aponta como "cabeça" a próxima e remove a tarefa                  
        anterior = None               # Decrementa a quantidade de tarefas
        while atual is not None:      # Se não encontrou a tarefa ou sucedeu, emite uma mensagem ao usuário                
            if atual.numero == numero:                  
                if anterior is None:                    
                    self.cabeca = atual.proximo         
                else:
                    anterior.proximo = atual.proximo    
                
                self.quantidade -= 1                    
                print(f"Tarefa {numero} removida.")
                return
            
            anterior = atual                            
            atual = atual.proximo

        print(f"Tarefa {numero} não encontrada.")       

    def buscar_tarefa(self, numero):  # Percorre a lista até encontrar tafera referente ao número indicado, atualiza a posição ou retorna ela 
        atual = self.cabeca                           
        posicao = 0
        while atual is not None:
            if atual.numero == numero:
                return posicao
            atual = atual.proximo
            posicao += 1
        return -1

    def exibir_tarefas(self):         # Percorre a lista a partir da "cabeça" 
        atual = self.cabeca           # Imprime cada tarefa na ordem do número ID, também imprime a quantidade de tarefas nela 
        print("Lista de Tarefas:")
        while atual is not None:
            print(f"Tarefa {atual.numero}", end=" -> ")
            atual = atual.proximo
        print("None")
        print(f"Tamanho da Lista: {self.quantidade}")


def menu():
    lista = ListaDeTarefas()
    
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar tarefa no início")
        print("2. Adicionar tarefa no fim")
        print("3. Remover tarefa")
        print("4. Buscar tarefa")
        print("5. Exibir tarefas")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                numero = int(input("Digite o número da tarefa para adicionar no início: "))
                lista.adicionar_no_inicio(numero)
            case "2":
                numero = int(input("Digite o número da tarefa para adicionar no fim: "))
                lista.adicionar_no_fim(numero)
            case "3":
                numero = int(input("Digite o número da tarefa para remover: "))
                lista.remover_tarefa(numero)
            case "4":
                numero = int(input("Digite o número da tarefa para buscar: "))
                posicao = lista.buscar_tarefa(numero)
                if posicao == -1:
                    print(f"Tarefa {numero} não encontrada.")
                else:
                    print(f"Tarefa {numero} encontrada na posição {posicao}.")
            case "5":
                lista.exibir_tarefas()
            case "6":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

menu()