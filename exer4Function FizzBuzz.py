"""
Exercício 4 Function - aula 50 - FizzBuzz
"""

def texto(n1):

    if n1 % 3 == 0 and n1 % 5 == 0:
        return f'FizzBuzz. O número {n1} é divisível por 3 e 5'
    if n1 % 3 == 0:
        return f'Fizz. O número {n1} é divisível por 3'
    if n1 % 5 == 0:
        return f'Buzz. O número {n1} é divisível por 5'

    return n1

resultado = texto(15)
print(resultado)