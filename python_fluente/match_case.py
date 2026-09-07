def handle_command(self, message):
    """
    Processa comandos recebidos via mensagem usando pattern matching.
    
    Args:
        message: Lista contendo o comando e seus parâmetros
    """
    match message:
        case ['BEEPER', frequency, times]:
            # Aciona o beeper com frequência e número de vezes especificados
            self.beep(times, frequency)
            
        case ['NECK', angle]:
            # Rotaciona o pescoço para o ângulo especificado
            self.rotate_neck(angle)
            
        case ['LED', pin, intensity]:
            # Ajusta o brilho do LED no pino especificado
            self.leds[pin].set_brightness(intensity)  # Corrigido: 'ident' -> 'pin'
            
        case ['LED', pin, red, green, blue]:
            # Define a cor RGB do LED no pino especificado
            self.leds[pin].set_color(red, green, blue)  # Corrigido: 'ident' -> 'pin', ordem dos parâmetros
            
        case _:
            # Comando inválido ou não reconhecido
            raise InvalidCommand(message)
        

beeper = ('beeper', 440, 3)
print(beeper)

print()

# Lista de áreas metropolitanas com informações geográficas
# Formato: (nome, código do país, população em milhões, (latitude, longitude))
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    # Exibe cabeçalho da tabela
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    
    # Itera sobre cada registro de área metropolitana
    for record in metro_areas:
        # Usa pattern matching para desestruturar o registro
        match record:
            # Captura nome e coordenadas, filtra apenas cidades no hemisfério ocidental (longitude <= 0)
            case [name, _, _, (lat, lon)] if lon <= 0:
                # Exibe o nome da cidade e suas coordenadas formatadas
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

# Executa a função principal
print("\nCidades no Hemisfério Ocidental:")
print("-" * 45)
main()

print()

# ====================================================================
# DEFINIÇÕES AUXILIARES (necessárias para o interpretador Scheme/Lisp)
# ====================================================================

from typing import Any
from collections import ChainMap

# Tipo para símbolos (nomes de variáveis em Lisp/Scheme)
class Symbol(str):
    """Símbolo - representa um nome de variável ou função."""
    pass

# Tipo para expressões (pode ser símbolo, número, lista, etc)
Expression = Symbol | list

# Ambiente para armazenar variáveis (como um dicionário)
Environment = ChainMap

# Classe para representar uma função (closure)
class Procedure:
    """Representa uma função lambda em Scheme."""
    def __init__(self, parms, body, env):
        self.parms = parms  # parâmetros da função
        self.body = body    # corpo da função
        self.env = env      # ambiente onde foi definida (closure)
    
    def __repr__(self):
        return f"<Procedure parms={self.parms}>"


# ====================================================================
# VERSÃO CLÁSSICA (if/elif) - funciona em qualquer versão do Python
# ====================================================================

def evaluate(exp: Expression, env: Environment) -> Any:
    """Avalia uma expressão em um ambiente (interpretador Scheme/Lisp)."""
    
    # Referência a variável - retorna o valor armazenado no ambiente
    if isinstance(exp, Symbol):
        return env[exp]
    
    # ... lines omitted
    
    # Expressão quote - retorna o valor literal sem avaliar
    elif exp[0] == 'quote':          # (quote exp)
        (_, x) = exp
        return x
    
    # Expressão condicional if - avalia teste e retorna consequência ou alternativa
    elif exp[0] == 'if':             # (if test conseq alt)
        (_, test, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    
    # Expressão lambda - cria uma função (closure)
    elif exp[0] == 'lambda':         # (lambda (parm…) body…)
        (_, parms, *body) = exp
        return Procedure(parms, body, env)
    
    # Expressão define - define uma variável no ambiente
    elif exp[0] == 'define':
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)
    
    # ... more lines omitted


print("\n" + "="*70)
print("VERSÃO REFATORADA COM MATCH/CASE (Python 3.10+)")
print("="*70 + "\n")

def evaluate_refactored(exp: Expression, env: Environment) -> Any:
    """
    Avalia uma expressão em um ambiente (interpretador Scheme/Lisp).
    VERSÃO REFATORADA usando pattern matching (Python 3.10+).
    """
    match exp:
        # Referência a variável - retorna o valor armazenado no ambiente
        case Symbol() as name:  # (1)
            return env[name]
        
        # Expressão quote - retorna o valor literal sem avaliar
        case ['quote', x]:  # (2)
            return x
        
        # Expressão condicional if - avalia teste e retorna consequência ou alternativa
        case ['if', test, consequence, alternative]:  # (3)
            if evaluate_refactored(test, env):
                return evaluate_refactored(consequence, env)
            else:
                return evaluate_refactored(alternative, env)
        
        # Expressão lambda - cria uma função (closure)
        # Guard 'if body' garante que body não está vazio
        case ['lambda', [*parms], *body] if body:  # (4)
            return Procedure(parms, body, env)
        
        # Expressão define - define uma variável no ambiente
        # Symbol() valida o tipo e 'as name' captura o valor
        case ['define', Symbol() as name, value_exp]:  # (5)
            env[name] = evaluate_refactored(value_exp, env)
        
        # Caso padrão - expressão inválida
        case _:  # (6)
            # Para valores literais (números, booleanos, strings), retorna o próprio valor
            if isinstance(exp, (int, float, bool, str)) and not isinstance(exp, Symbol):
                return exp
            raise SyntaxError(f"Expressão inválida: {exp}")


# COMPARAÇÃO ENTRE AS DUAS ABORDAGENS:
print("""
PRINCIPAIS DIFERENÇAS:

1. CHECAGEM DE TIPO:
   Antiga: if isinstance(exp, Symbol)
   Nova:   case Symbol() as name
   
2. DESEMPACOTAMENTO:
   Antiga: (_, x) = exp  após checar exp[0] == 'quote'
   Nova:   case ['quote', x]
   
3. GUARDS (VALIDAÇÕES):
   Antiga: Não há validação se body está vazio
   Nova:   case ['lambda', [*parms], *body] if body
   
4. LEGIBILIDADE:
   Antiga: Múltiplos if/elif com acesso repetido a exp[0]
   Nova:   Padrões declarativos que mostram a estrutura esperada
   
5. CAPTURA COM VALIDAÇÃO:
   Antiga: Checagem separada do tipo Symbol
   Nova:   Symbol() as name valida e captura simultaneamente

RELAÇÃO COM ITERÁVEIS/ITERADORES:
- ['quote', x]: Python itera sobre exp para fazer pattern matching
- [*parms]: Captura zero ou mais elementos (usa __iter__ internamente)  
- *body: Captura elementos restantes (também usa iteração)
- O match/case utiliza o protocolo de iteração para desempacotar sequências
""")


# ====================================================================
# EXEMPLOS PRÁTICOS - EXECUTANDO AS FUNÇÕES
# ====================================================================

print("\n" + "="*70)
print("EXEMPLOS PRÁTICOS - EXECUTANDO AS FUNÇÕES")
print("="*70 + "\n")

# Cria um ambiente com algumas variáveis predefinidas
env = ChainMap({'x': 10, 'y': 20, '+': lambda a, b: a + b})

print("🔹 Ambiente inicial:", dict(env))
print()

# EXEMPLO 1: Expressão quote - retorna valor literal
print("EXEMPLO 1: Expressão QUOTE")
print("-" * 40)
exp1 = ['quote', [1, 2, 3]]
print(f"Expressão: {exp1}")
print(f"Resultado: {evaluate_refactored(exp1, env)}")
print("Explicação: 'quote' retorna o valor literal sem avaliar")
print()

# EXEMPLO 2: Referência a variável
print("EXEMPLO 2: Referência a VARIÁVEL")
print("-" * 40)
exp2 = Symbol('x')
print(f"Expressão: {exp2}")
print(f"Resultado: {evaluate_refactored(exp2, env)}")
print("Explicação: Busca o valor de 'x' no ambiente (retorna 10)")
print()

# EXEMPLO 3: Expressão if (condicional)
print("EXEMPLO 3: Expressão IF (condicional)")
print("-" * 40)
# if x > 5 then y else 0
# Em Lisp: (if (> x 5) y 0)
# Simplificado para demonstração: (if True y 0)
exp3 = ['if', True, Symbol('y'), 0]
print(f"Expressão: {exp3}")
print(f"Resultado: {evaluate_refactored(exp3, env)}")
print("Explicação: Se True, retorna y (20), senão retorna 0")
print()

exp3_false = ['if', False, Symbol('y'), 999]
print(f"Expressão: {exp3_false}")
print(f"Resultado: {evaluate_refactored(exp3_false, env)}")
print("Explicação: Se False, retorna a alternativa (999)")
print()

# EXEMPLO 4: Lambda (criando uma função)
print("EXEMPLO 4: LAMBDA (criando função)")
print("-" * 40)
exp4 = ['lambda', [Symbol('a'), Symbol('b')], ['quote', 'corpo da função']]
print(f"Expressão: {exp4}")
resultado = evaluate_refactored(exp4, env)
print(f"Resultado: {resultado}")
print("Explicação: Cria uma função com parâmetros [a, b]")
print()

# EXEMPLO 5: Define (definindo nova variável)
print("EXEMPLO 5: DEFINE (definindo variável)")
print("-" * 40)
exp5 = ['define', Symbol('z'), 100]
print(f"Expressão: {exp5}")
print(f"Ambiente ANTES: {dict(env)}")
evaluate_refactored(exp5, env)
print(f"Ambiente DEPOIS: {dict(env)}")
print("Explicação: Define z = 100 no ambiente")
print()

# EXEMPLO 6: Demonstrando desempacotamento com *
print("EXEMPLO 6: DESEMPACOTAMENTO com * (iteração)")
print("-" * 40)
exp6 = ['lambda', [Symbol('x')], ['quote', 'linha1'], ['quote', 'linha2'], ['quote', 'linha3']]
print(f"Expressão: {exp6}")
print("Estrutura: ['lambda', [parâmetros], *body]")
print("           onde *body captura: [['quote', 'linha1'], ['quote', 'linha2'], ['quote', 'linha3']]")
resultado6 = evaluate_refactored(exp6, env)
print(f"Resultado: {resultado6}")
print(f"Body capturado (múltiplos elementos): {resultado6.body}")
print("Explicação: O *body usa iteração para capturar todos elementos restantes")
print()

print("="*70)
print("CONCLUSÃO: O pattern matching facilita o desempacotamento de")
print("estruturas iteráveis complexas de forma declarativa e legível!")
print("="*70)