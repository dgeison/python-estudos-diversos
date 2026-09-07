def smash_to_sentence(words):
    """Concatena palavras em uma frase usando join."""
    return " ".join(words)


def smash_with_loop(words):
    """Concatena palavras em uma frase usando loop.
    
    Retorna um espaço se a lista estiver vazia.
    """
    if not words:
        return " "
    sentence = words[0]
    for word in words[1:]:
        sentence += " " + word
    return sentence


def smash_with_comprehension(words):
    """Concatena palavras em uma frase usando list comprehension.
    
    Retorna um espaço se a lista estiver vazia.
    """
    if not words:
        return " "
    return " ".join([word for word in words])


# Lista de palavras para teste
words = ["hello", "world", "this", "is", "great"]

# Testa as três implementações
print(smash_to_sentence(words))
print(smash_with_loop(words))
print(smash_with_comprehension(words))


def filtrar_aprovados(notas):
    """Filtra alunos com nota >= 7.0 e retorna nomes ordenados alfabeticamente.
    
    Args:
        notas: Dicionário onde a chave é o nome do aluno e o valor é a nota (float).
    
    Returns:
        Lista contendo apenas os nomes dos aprovados, ordenados alfabeticamente.
    """
    aprovados = [nome for nome, nota in notas.items() if nota >= 7.0]
    return sorted(aprovados)


# Exemplo de uso
notas_turma = {
    "João": 8.5,
    "Maria": 6.0,
    "Ana": 9.0,
    "Pedro": 5.5,
    "Bia": 7.0
}

print("Alunos aprovados:", filtrar_aprovados(notas_turma))
