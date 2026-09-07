def alphabet_position(text):
    """
    Converte cada letra de um texto em sua posição no alfabeto.
    A função percorre o texto caractere por caractere, ignorando tudo que não seja letra,
    e retorna uma string com as posições numéricas separadas por espaços.
    Args:
        text (str): O texto a ser convertido.
    Returns:
        str: String contendo as posições das letras separadas por espaço.
             Exemplo: "abc" retorna "1 2 3"
    Example:
        >>> alphabet_position("Hello World")
        "8 5 12 12 15 23 15 18 12 4"
    Note:
        A implementação usa `ord(caracter) - ord('a') + 1` em vez de `ord(caracter) - 96`
        por questão de legibilidade e manutenibilidade do código. Embora matematicamente
        equivalentes (já que ord('a') = 97, então 97 - 1 = 96), a primeira forma deixa
        explícita a intenção: calcular a distância entre o caractere e 'a', depois ajustar
        para começar em 1. Isso torna o código auto-documentável e menos suscetível a erros
        caso o encoding mude, além de ser mais fácil de entender para outros desenvolvedores.
    """
    resultado = []  # onde vou guardar os números
    
    for caracter in text.lower():  # percorro tudo em minúsculo
        if 'a' <= caracter <= 'z':  # só letras
            posicao = ord(caracter) - ord('a') + 1  # 'a' vira 1
            resultado.append(str(posicao))  # adiciono como string
    
    return ' '.join(resultado)  # junto tudo com espaços


# Versão com list comprehension (mais pythônica)
def alphabet_position_pythonic(text):
    return ' '.join(
        str(ord(c) - 96) 
        for c in text.lower() 
        if c.isalpha()
    )



input = "a pipa"

print(alphabet_position(input))

97 - 97 + 1