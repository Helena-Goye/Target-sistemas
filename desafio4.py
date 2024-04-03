interruptores = [False, False, False]  #false representa o interruptor desligado
lampadas = [False, False, False]       #false representa a lâmpada apagada

#lógica para descobrir qual interruptor controla cada lâmpada
def descobrir_interruptores(interruptores, lampadas):
    #ligar o primeiro interruptor
    interruptores[0] = True

    print("Primeiro interruptor ligado.")

    #desligar o primeiro interruptor e ligar o segundo interruptor
    interruptores[0] = False
    interruptores[1] = True

    print("Segundo interruptor ligado.")

    #verificar o estado das lâmpadas
    for i, lampada in enumerate(lampadas):
        if lampada:
            print(f"A lâmpada {i + 1} está acesa e está conectada ao interruptor {i + 1}.")
        else:
            print(f"A lâmpada {i + 1} está apagada e está conectada ao interruptor {i + 1}.")

#função para descobrir qual interruptor controla cada lâmpada
descobrir_interruptores(interruptores, lampadas)