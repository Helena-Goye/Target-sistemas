#função para verificar se um número pertence à sequência de Fibonacci
def verifica_fibonacci(numero):
    a, b = 0, 1
    fibonacci = [a, b]

 #calcula os números da sequência de Fibonacci até que b seja >= ao número digitado
    while b < numero:
        a, b = b, a + b
        fibonacci.append(b)

 #verificar se o número está na sequência de Fibonacci e exibir uma mensagem
    if numero in fibonacci:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
        return True
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
        return False

#Loop principal que solicita continuamente um número ao usuário

while True:
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if verifica_fibonacci(numero):
        break  #se o número pertence à sequência, o loop é interrompido

    else:
        continue #se não pertence, continua o loop e solicita outro número ao usuário
