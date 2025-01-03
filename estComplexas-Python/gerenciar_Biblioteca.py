class PilhaDeLivros:
    def __init__(self):               # Inicializa uma lista para representar a pilha de livros
        self.livros = []              
        
    def is_empty(self):               # Verifica se a pilha de livros está vazia
        return len(self.livros) == 0
        
    def adicionar_livro(self, livro): # Adiciona um novo livro ao topo da pilha
        self.livros.append(livro)
        print(f"O livro '{livro}' foi adicionado à pilha.")
        
    def retirar_livro(self):          # Remove e retorna o livro no topo da pilha
        if self.is_empty():
            raise Exception("A pilha de livros está vazia!")
        return self.livros.pop()
        
    def livro_no_topo(self):          # Retorna o livro no topo da pilha sem removê-lo              
        if self.is_empty():
            raise Exception("A pilha de livros está vazia!")
        return self.livros[-1]
        
    def quantidade_livros(self):      # Retorna o número de livros na pilha
        return len(self.livros)
 
# Programa principal
if __name__ == "__main__":
    pilha_de_livros = PilhaDeLivros()
 
    pilha_de_livros.adicionar_livro("1984")
    pilha_de_livros.adicionar_livro("O Senhor dos Anéis")
    pilha_de_livros.adicionar_livro("Dom Quixote")
    pilha_de_livros.adicionar_livro("Moby Dick")
    pilha_de_livros.adicionar_livro("A Revolução dos Bichos")
 
    print(f"Livro retirado: {pilha_de_livros.retirar_livro()}")
    print(f"Livro retirado: {pilha_de_livros.retirar_livro()}")
 
    print(f"Livro no topo da pilha: {pilha_de_livros.livro_no_topo()}")
 
    print(f"Quantidade de livros restantes: {pilha_de_livros.quantidade_livros()}")