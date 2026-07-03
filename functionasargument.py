def double(x):
    return x * 2

# Define uma função chamada "double" que aceita um argumento x e retorna o seu dobro. 

def apply_to_one(f):
    return f(1)

# Define uma função chamada "apply_to_one" que recebe outra função como argumento (f)
# e a executa passando o número 1 como parâmetro 

my_double = double

# Cria uma variável chamada "my_double" que aponta para a mesma função que "double"
# (Funções em Python são objetos de primeira classe e podem ser atribuídas a variáveis).

x = apply_to_one(my_double)

# Passa a função "my_double" como argumento para "apply_to_one".
# O Python executa my_double(1), que retorna 2, e guarda esse resultado. 

print(x)

# Mostra o resultado no terminal
