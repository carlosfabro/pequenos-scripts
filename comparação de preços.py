# obter dados sobre os produtos
valor_produtoa = float(input("insira aqui o valor do produto a: "))
unidade_produtoa = float(input("insira aqui quantas unidades de uso do produto a possui: "))

valor_produtob = float(input("insira aqui o valor do produto b:  "))
unidade_produtob = float(input("insira aqui quantas unidades de uso do produto b possui: "))

# calcular qual o valor por unidade dos produtos
valor_unidadea = valor_produtoa/unidade_produtoa
valor_unidadeb = valor_produtob/unidade_produtob

# dizer qual produto esta com um valor melhor
if valor_unidadea < valor_unidadeb:
    print("O produto A esta realmente com um valor melhor")
if valor_unidadea > valor_unidadeb:
    print("O produto B esta realmente com um valor melhor")
    if valor_unidadea == valor_unidadeb:
    print("ambos estão com um valor similar")
    
