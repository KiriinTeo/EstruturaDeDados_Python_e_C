estoque = {
    "camisas": 50, 
    "calças": 30,
    "sapato": 20
}

print("Estoque Inicial:")
for item, quantidade in estoque.items():
    print(f"{item.capitalize()}: {quantidade}")
    
novo_item = input("DIgite o nome do novo item para adicionar ao estoque:") 
quantidade_nova = int(input("Digite a quantidade do novo item:")) 
estoque[novo_item] = quantidade_nova 

print("Estoque após adicionar novo item:")
for item, quantidade in estoque.items():
    print(f"{item.capitalize()}: {quantidade}") 

item_para_remover = input("Digite o nome do item para ser removido do estoque:") 
if item_para_remover in estoque: 
    estoque.pop(item_para_remover)

print("Estoque após remoção:")
for item, quantidade in estoque.items():
    print(f"{item.capitalize()}: {quantidade}") 