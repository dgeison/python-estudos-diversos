# Abordagem tradicional usando loop for:
# - Cria uma lista vazia
# - Itera sobre cada símbolo
# - Adiciona cada código Unicode à lista usando append()
# - Mais verboso, mas mais fácil de entender para iniciantes
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)




# Abordagem usando list comprehension (compreensão de lista):
# - Cria a lista em uma única linha
# - Mais concisa e pythônica
# - Geralmente mais rápida que o loop for tradicional
# - Preferida quando a operação é simples e direta
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)


# Separador visual entre os exemplos
print('\n' + '-' * 40 + '\n')
# Exemplo mostrando o escopo de variáveis em list comprehension

x = 'ABC'
codes = [ord(x) for x in x]
print(x)  # (1) Saída: 'ABC'

print(codes)  # Saída: [65, 66, 67]

codes = [last := ord(c) for c in x]
print(last)  # (2) Saída: 67

# Tentando acessar 'c' causaria erro pois está no escopo da comprehension:
# print(c)  # (3) NameError: name 'c' is not defined