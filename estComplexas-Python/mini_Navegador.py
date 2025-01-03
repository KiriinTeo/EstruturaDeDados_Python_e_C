class Navegar:
    def __init__(self):
        self.acoes = []  # Pilha
        self.redo_stack = []  # Pilha de ações desfeitas (para refazer).

    def adicionar_acao(self, acao):  # Adiciona uma nova ação à pilha de ações e limpa a pilha de refazer.
        self.acoes.append(acao)
        self.redo_stack.clear() 
        print(f'Pesquisa registrada: "{acao}"')  
    def desfazer_acao(self):
        if self.acoes:
            acao = self.acoes.pop()  # Remove a última ação da lista de ações.
            self.redo_stack.append(acao)  # Coloca a ação desfeita na pilha de redo (refazer).
            print(f'Pesquisa desfeita: "{acao}"')  
        else:
            print('Não há pesquisas para desfazer.')  # Informa que não há ações para desfazer.

    def refazer_acao(self):
        if self.redo_stack:
            acao = self.redo_stack.pop()  # Remove a última ação da lista de refazer.
            self.acoes.append(acao)  
            print(f'Pesquisa refeita: "{acao}"')  
        else:
            print('Não há Pesquisas para refazer.')  

    def exibir_acoes(self):
        if self.acoes:
            print('Historico de pesquisas:')
            for acao in self.acoes:  # Itera sobre a lista de ações e as exibe.
                print(f'- {acao}')
        else:
            print('Nenhuma Pesquisa registrada.')  
    def pode_desfazer(self):
        return len(self.acoes) > 0

    def pode_refazer(self):
        return len(self.redo_stack) > 0

def main():
    editor = Navegar()

    while True:
        print("\nEscolha uma opção:")
        print("1. Realizar uma pesquisa")
        print("2. Desfazer Pesquisa")
        print("3. Refazer Pesquisa")
        print("4. Exibir Historico")
        print("5. Sair")
        
        # Lê a escolha do usuário.
        escolha = input("Digite o número da opção: ")

        # Verifica qual opção foi escolhida e executa a ação correspondente.
        if escolha == '1':
            acao = input("Digite sua nova pesquisa: ")  
            editor.adicionar_acao(acao)  
        elif escolha == '2':
            editor.desfazer_acao()  
        elif escolha == '3':
            editor.refazer_acao() 
        elif escolha == '4':
            editor.exibir_acoes()  
        elif escolha == '5':
            print("Saindo...")  # Sai do programa.
            break  # Interrompe o loop, encerrando o programa.
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro 

if __name__ == "__main__":
    main()
