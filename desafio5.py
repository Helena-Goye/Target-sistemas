#função para inverter uma string
def inverter_string(s):
    return s[::-1]

#string original
string_original = "Target Sistemas"

#inverter a string
string_invertida = inverter_string(string_original)

#exibindo a string invertida
print("String original:", string_original)
print("String invertida:", string_invertida)