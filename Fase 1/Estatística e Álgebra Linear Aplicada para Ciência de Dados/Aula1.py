import numpy as np

# Definir a matriz dos coeficientes A
A = np.array([[2, 3], 
              [5, 7]])

# Definir o vetor dos termos independentes B
B = np.array([8, 19])

# Resolver o sistema
solucao = np.linalg.solve(A, B)

print(f"Valores de x e y: {solucao}")


Valores de x e y: [1. 2.]


from scipy.linalg import solve

solucao = solve(A, B)
print(f"Valores de x e y: {solucao}")


from sympy import symbols, Eq, solve

# Definir variáveis
x, y = symbols('x y')

# Definir as equações
eq1 = Eq(2*x + 3*y, 8)
eq2 = Eq(5*x + 7*y, 19)

# Resolver o sistema
solucao = solve((eq1, eq2), (x, y))
print(solucao)


# Criando matrizes 
import numpy as np

# Criando matrizes A e B
A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

print("Matriz A:\n", A)
print("Matriz B:\n", B)

#Adicao de matrizes 

C = A + B  # Ou np.add(A, B)
print("Soma das matrizes:\n", C)


#Subtracao de matrizes 
C = A - B  # Ou np.subtract(A, B)
print("Subtração das matrizes:\n", C)

#Multiplicacao de matrizes 
C = A * B  # Ou np.multiply(A, B)
print("Multiplicação elemento a elemento:\n", C)



#Espaco vetorial 
import numpy as np

# Definição de dois vetores em R²
v1 = np.array([1, 2])
v2 = np.array([3, 4])

# Soma de vetores
soma = v1 + v2
print("Soma dos vetores:", soma)

# Multiplicação por escalar
escalar = 2
multiplicacao = escalar * v1
print("Multiplicação por escalar:", multiplicacao)

#Autovalor e autovetor 
# Definição da matriz A
A = np.array([[4, -2], 
              [1, 1]])

# Cálculo dos autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)

print("Autovalores:", autovalores)
print("Autovetores:\n", autovetores)

