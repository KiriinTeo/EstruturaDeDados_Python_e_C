class No:
    def __init__(self, valor): # Define um número identificdor para o nó e aponta ao próximo.
        self.valor = valor
        self.proximo = None

class listaEncadeada:          # Inicializa a lista com uma inicial "cabeça" vazia.
    def __inti__(self):
        self.cabeca = None

    def adicionar_no_inicio(self, valor): # Adiciona um valor novo e define ele como "cabeça".
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
    
    def adicionar_no_fim(self, valor):    # Verifica se não há nó "cabeça", caso não haja, define ele assim.
        novo_no = No(valor)               # Caso haja outros nós na lista, percorre ela até seu fim e adiciona o nova nó lá.
        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no
        
    def buscar(self, valor):              # Percorre a lista até encontrar um nó na posição buscada.
        atual = self.cabeca               # Emite uma mensagem de posição encontrada ou não encontrada.
        posicao = 0
        while atual:
            if atual.valor == valor:
                return f"elemento {valor} encontrado a posição {posicao}"
            atual = atual.proximo
            posicao += 1 
        return f"Elemento {valor} não encontrado"
    
    def remover(self, valor):             # Verifica se a lista está vazia    
        if not self.cabeca:               # Percorre a lista até encontrar o valor ser removido e aponta para o próximo valor
            return "A lista está vazia"
            
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            return f"Elemento {valor} removido."
            
        atual = self.cabeca
        anterior = None
        while atual: 
            if atual.valor == valor:
                anterior.proximo == atual.proximo
                return f"Elemento {valor} removido."
            anterior = atual
            atual = atual.proximo
            
        return f"Elemento {valor} não encontrado."
    
    def percorrer_lista(self):             # Percorre e imprime a lista.
        atual = self.cabeca
        while atual:
            print(atual.valor, end = ' -> ')
            atual = atual.proximo
        print("None")
    
        lista = listaEncadeada()
        lista.adicionar_no_inicio(5)
        lista.adicionar_no_inicio(3)
        lista.adicionar_no_fim(7)
        
print("Lista Completa:")
listaEncadeada.percorer_lista()
        
print(listaEncadeada.buscar(7))
        
listaEncadeada.remover(3)
print("Lista completa após remoção:")
listaEncadeada.percorrer_lista()