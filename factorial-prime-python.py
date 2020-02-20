#Primeiro eu defini uma função que calcule a sequencia de Fibonacci, mas que nao dê um valor maior do que 1.000.000
def fibonacci(x):
  fib0 = 0
  fib1 = 1
  yield fib0 #Para o resultado final que se pede, esse yield é dispensável. Ele serve apenas para exibir o 0 no início da sequência de Fibonacci
  
  while (x>0):
    temp = fib0
    fib0 = fib1 
    fib1 = fib1 + temp
    x = x-1
    yield fib0
    if fib0>=1000000:
      break

#Depois eu criei uma função que encontre os números primos de um intervalo, a partir do Crivo de Erastótenes
def crivo(x):
  A = [True] * (x+1)
  A[0] = A[1] = False

  for indice, primo in enumerate(A):
    if primo:
      yield indice
      for i in range(indice*2, x+1, indice):
        A[i] = False

#Em seguida eu criei duas listas que recebem os valores primos e da sequencia de Fibonacci menores do que 1.000.000
lista_crivo = (list(crivo(1000000)))
lista_fibonacci = (list(fibonacci(1000000)))

#Criei uma lista apenas com os valores que estejam presentes tanto na lista_crivo quanto na lista_fibonacci
lista_final = [x for x in lista_fibonacci if x in lista_crivo]

#Somei todos os elementos da lista_final 
soma = sum(lista_final)
print(soma)










