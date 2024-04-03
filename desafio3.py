#sequência A
seq_a = [1, 3, 5, 7]
prox_a = seq_a[-1] + 2  #próximo elemento é o último elemento da sequência +2
seq_a.append(prox_a)
print("Próximo elemento de A é:", seq_a)

#sequência B
seq_b = [2, 4, 8, 16, 32, 64]
prox_b = seq_b[-1] * 2  #próximo elemento é o último elemento da sequência ×2 
seq_b.append(prox_b)
print("Próximo elemento de B é:", seq_b)

#sequência C
seq_c = [0, 1, 4, 9, 16, 25, 36]
prox_c = seq_c[-1] + 7  #próximo elemento é o último elemento da sequência +7
seq_c.append(prox_c)
print("Próximo elemento de C é:", seq_c)

#sequência D
seq_d = [4, 16, 36, 64]
prox_d = seq_d[-1] + 36  #próximo elemento é o último elemento da sequência +36
seq_d.append(prox_d)
print("Próximo elemento de D é:", seq_d)

#sequência E
seq_e = [1, 1, 2, 3, 5, 8]
prox_e = seq_e[-1] + seq_e[-2]  #próximo elemento é a soma dos dois últimos elementos da sequência
seq_e.append(prox_e)
print("Próximo elemento de E é:", seq_e)

#sequência F
seq_f = [2, 10, 12, 16, 17, 18, 19]
prox_f = seq_f[-1] + 1  #próximo elemento é o último elemento da sequência +1
seq_f.append(prox_f)
print("Próximo elemento de F é:", seq_f)