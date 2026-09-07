import math

class Vector:
    """
    Classe que representa um vetor 2D no plano cartesiano.
    
    Um vetor é como uma seta que aponta de um lugar para outro.
    Tem duas informações:
    - x: quanto vai para o lado (direita/esquerda)
    - y: quanto vai para cima/baixo
    
    Exemplo: Vector(3, 4) é uma seta que vai 3 unidades para direita e 4 para cima.
    """
    
    def __init__(self, x=0, y=0):
        """
        Construtor - cria um novo vetor.
        
        Args:
            x (float): Coordenada horizontal (padrão: 0)
            y (float): Coordenada vertical (padrão: 0)
            
        Exemplo:
            v1 = Vector(2, 4)  # Cria vetor com x=2, y=4
            v2 = Vector()      # Cria vetor com x=0, y=0 (padrão)
        """
        self.x=x
        self.y=y

    def __repr__(self):
        """
        Define como o vetor aparece quando você imprime ele.
        
        Sem isso, você veria algo feio tipo <__main__.Vector object at 0x...>
        Com isso, você vê Vector(2, 4) - muito mais claro!
        
        Returns:
            str: Representação legível do vetor
            
        Exemplo:
            v = Vector(2, 4)
            print(v)  # Saída: Vector(2, 4)
        """
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        """
        Calcula o COMPRIMENTO da seta (vetor) usando o Teorema de Pitágoras!
        
        math.hypot(x, y) calcula √(x² + y²)
        Para Vector(3, 4): √(3² + 4²) = √(9 + 16) = √25 = 5.0
        
        Por que 5? Imagine um triângulo retângulo: vai 3 para direita,
        4 para cima. A hipotenusa (seta) tem tamanho 5!
        
        Returns:
            float: O tamanho/magnitude do vetor
            
        Exemplo:
            v = Vector(3, 4)
            print(abs(v))  # Saída: 5.0
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        Verifica se o vetor "existe" ou é nulo (0, 0).
        
        - Se o tamanho é 0 → False (vetor nulo)
        - Se o tamanho é diferente de 0 → True
        
        Returns:
            bool: False se vetor for (0,0), True caso contrário
            
        Exemplo:
            v1 = Vector(3, 4)
            if v1:
                print("Vetor existe!")  # Isso imprime!
            
            v2 = Vector(0, 0)
            if not v2:
                print("Vetor é nulo!")  # Isso imprime!
        """
        return bool(abs(self))

    def __add__(self, other):
        """
        Soma dois vetores "coordenada por coordenada".
        
        - Soma os x's: 2 + 2 = 4
        - Soma os y's: 4 + 1 = 5
        - Cria novo vetor: Vector(4, 5)
        
        Analogia: É como andar 2 passos para direita e 4 para cima,
        depois mais 2 para direita e 1 para cima.
        Total: 4 direita, 5 cima!
        
        Args:
            other (Vector): Outro vetor para somar
            
        Returns:
            Vector: Novo vetor resultante da soma
            
        Exemplo:
            v1 = Vector(2, 4)  # Seta: 2 direita, 4 cima
            v2 = Vector(2, 1)  # Seta: 2 direita, 1 cima
            resultado = v1 + v2  # Resultado: 4 direita, 5 cima
            print(resultado)     # Vector(4, 5)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        Multiplica o vetor por um número (escalar), deixando a seta mais LONGA ou CURTA.
        
        Multiplica cada coordenada pelo número:
        Vector(3, 4) * 3 = Vector(9, 12)
        
        Se v tinha tamanho 5, multiplicar por 3 → tamanho 15
        
        Args:
            scalar (float): Número para multiplicar o vetor
            
        Returns:
            Vector: Novo vetor multiplicado (escalado)
            
        Exemplo:
            v = Vector(3, 4)
            print(v * 3)        # Vector(9, 12) - seta 3x maior
            print(abs(v * 3))   # 15.0 - tamanho também fica 3x maior!
        """
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    """
    EXEMPLOS DE USO DA CLASSE VECTOR
    
    Por que isso é poderoso?
    Esses "métodos mágicos" (com __) fazem o Python entender sua classe
    como se fosse um tipo nativo:
    - __add__ permite usar +
    - __mul__ permite usar *
    - __abs__ permite usar abs()
    - __repr__ faz o print() funcionar bem
    
    Sem eles, você teria que escrever v1.somar(v2) ao invés de v1 + v2!
    """
    
    # 1️⃣ SOMA DE VETORES (Addition)
    print("=== SOMA DE VETORES ===")
    v1 = Vector(2, 4)  # Vetor 1: 2 direita, 4 cima
    v2 = Vector(2, 1)  # Vetor 2: 2 direita, 1 cima
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")  # Resultado: 4 direita, 5 cima
    print()

    # 2️⃣ VALOR ABSOLUTO - Tamanho do vetor (Absolute value)
    print("=== TAMANHO DO VETOR ===")
    v = Vector(3, 4)
    print(f"v = {v}")
    print(f"abs(v) = {abs(v)}")  # Teorema de Pitágoras: √(3²+4²) = 5.0
    print()

    # 3️⃣ MULTIPLICAÇÃO POR ESCALAR (Scalar multiplication)
    print("=== MULTIPLICAÇÃO POR ESCALAR ===")
    print(f"v * 3 = {v * 3}")  # Vetor 3x maior: cada coordenada × 3
    print(f"abs(v * 3) = {abs(v * 3)}")  # Tamanho também fica 3x maior: 15.0
    print()