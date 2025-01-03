class No: 
    def __init__ (self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def esta_vazia(self):
        return self.raiz is None
        
    def inserir_raiz(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            print(f"Produto {valor} adicionado com sucesso.\n")
        else:
            #print("Produto já existente.\n")
            return None
        
    def inserir_esquerda(self, valor_pai, valor):
        pai = self.buscar(self.raiz, valor_pai)
        if pai:
            if pai.esquerda is None:
                pai.esquerda = No(valor)
                print(f"Produto: {valor} foi incluído.\n")
            else:
                print(f"Este produto já foi incluído.\n")
        else:
            print(f"ERRO - {valor_pai} não encontrado.\n")
            
    def inserir_direita(self, valor_pai, valor):
        pai = self.buscar(self.raiz, valor_pai)
        if pai:
            if pai.direita is None:
                pai.direita = No(valor)
                print(f"Produto: {valor} foi incluído.\n")
            else:
                print(f"Este produto já foi incluído.\n")
        else:
            print(f"ERRO - {valor_pai} não encontrado.\n")

    def buscar(self, no, valor):
        if no is None:
            return None
        if no.valor == valor:
            return no
            
        esquerda = self.buscar(no.esquerda, valor)
        if esquerda is not None:
            return esquerda
        return self.buscar(no.direita, valor)

    def exibir_em_ordem(self, no):
        if no:
            self.exibir_em_ordem(no.esquerda)
            print("Ordem Produtos:", no.valor, end=" " "\n")
            self.exibir_em_ordem(no.direita)

    def contar_nos(self, no):
        if no is None:
            return 0
        return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)

    def excluir(self, valor):
        self.raiz, excluido = self._excluir(self.raiz, valor)
        if excluido:
            print(f"Produto {valor} excluído com sucesso.\n")
        else:
            print(f"Produto {valor} não encontrado.\n")

    def _excluir(self, no, valor):
        if no is None:
            return no, False
            
        if valor < no.valor:
            no.esquerda, excluido = self._excluir(no.esquerda, valor)
            return no, excluido
            
        elif valor > no.valor:
            no.direita, excluido = self._excluir(no.direita, valor)
            return no, excluido
            
        else:
            if no.esquerda is None and no.direita is None:
                return None, True
                
            elif no.esquerda is None:
                return no.direita, True
                
            elif no.direita is None:
                return no.esquerda, True
                
            else:
                sucessor = self._encontrar_minimo(no.direita)
                no.valor = sucessor.valor
                no.direita, _ = self._excluir(no.direita, sucessor.valor)
                return no, True

    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
        
def __menu__():
    
    acesso = ArvoreBinaria()
    valores = []
    prods = []
    
    while True:
        
        print("\nMenu de Operações.")
        print("1 - Inserir produto novo.")
        print("2 - Exibir produtos")
        print("3 - Quantidade de produtos.")
        print("4 - Excluir produtos.")
        print("Escolha qualquer outro númeoro para sair.")
        
        secao = int(input("\nDigite a operação desejada: "))
        
        if secao == 1:
            i = -1
            produto = input("\nQual produto será adicionado?: ")
            
            if acesso.esta_vazia():
                acesso.inserir_raiz(produto)
                
            preco = float(input("E qual seu preço?: "))
            valores.append(preco)
            
            if len(prods) > 0:
                if preco < min(valores):
                    acesso.inserir_esquerda(prods[i], produto)
                else:
                    acesso.inserir_direita(prods[i], produto)
                    
            prods.append(produto)        
                    
            i += 1
            
        elif secao == 2:
            acesso.exibir_em_ordem(acesso.raiz)
            valores.sort()  
            print(f"Preços: {valores}")
            print(f"Maior Preço: {max(valores)}")
            print(f"Menor Preço: {min(valores)}")
            
        elif secao == 3:
            print(f"Quantidade de produtos: {acesso.contar_nos(acesso.raiz)}") 
            
        elif secao == 4:
            produto_excluir = input("\nInforme um produto à ser excluído: ")
            acesso.excluir(produto_excluir)
    
        else:
            saida = int(input("Número Inválido, deseja sair?\n1 = Sim \nQualquer = Não\n"))
            if saida == 1:
                break
        
__menu__()