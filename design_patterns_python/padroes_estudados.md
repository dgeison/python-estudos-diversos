# Padrões de Design — Anotações de Aula

## Índice
- [Criacionais](#criacionais)
  - [Singleton](#singleton)

---

## Criacionais

### Singleton

**Ideia central:** Garantir que exista apenas **uma instância** de uma classe e fornecer um **ponto global de acesso** a ela.

**Muito usado para:** configuração global, logger, conexão com banco de dados, recursos compartilhados.

---

#### Forma 1 — `get_instance()` (estilo livro / outras linguagens)

Construtor privado simulado + método de classe que controla a criação.

```python
# singleton1_1.py
import json
from pprint import pprint

class ConfigSingleton:
    NOME_ARQUIVO = "config.json"
    _instancia = None

    def __init__(self):
        with open(self.NOME_ARQUIVO, "r") as f:
            self.dados = json.load(f)

    @classmethod
    def get_instance(cls):
        if cls._instancia is None:
            print("Criando a instância única")
            ConfigSingleton._instancia = ConfigSingleton()
        return ConfigSingleton._instancia

def main():
    s1 = ConfigSingleton.get_instance()
    s2 = ConfigSingleton.get_instance()
    pprint(s1.dados)
    print(f"s1 is s2: {s1 is s2}")   # True  — mesma instância

    s3 = ConfigSingleton()            # ATENÇÃO: burla o Singleton!
    print(f"s1 is s3: {s1 is s3}")   # False — instância diferente
```

---

**Por que `@classmethod`?**

Um método comum precisa de uma instância (`self`) para ser chamado.  
`@classmethod` recebe a **classe** (`cls`) em vez da instância — permite chamar `Config.get_instance()` sem ter um objeto criado ainda, que é exatamente o que precisamos.

```
Config.get_instance()   ✅  cls = Config
instancia.get_instance() ✅  também funciona, mas não é o uso esperado
```

---

**Por que `Config._instancia = Config()`?**

`Config()` chama `__init__`, cria o objeto e carrega o JSON.  
Esse objeto é salvo em `Config._instancia` (atributo da **classe**, não da instância).  
Na próxima chamada, `_instancia` já não é `None`, então retorna o mesmo objeto sem recriar.

```
1ª chamada: _instancia é None → cria Config() → salva em _instancia → retorna
2ª chamada: _instancia já existe → retorna direto (sem recriar)
```

---

**Limitação:** Python não tem construtor realmente privado. `Config()` direto burla o padrão (veja `s3` no exemplo). Para impedir isso, levante um erro no `__init__` se já existir instância.

> Estilo adotado em Java/C++. Explícito e fácil de entender.

---

#### Forma 2 — Sobrescrevendo `__new__` (mais robusto e pythônico)

```python
# singleton1_2.py
import json
from pprint import pprint

class Singleton:
    NOME_ARQUIVO = "config.json"
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando nova instância de ConfigSingleton")
            cls._instancia = super().__new__(cls)
            with open(cls.NOME_ARQUIVO, "r") as f:
                cls._instancia.dados = json.load(f)
        return cls._instancia

def main():
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)           # True

    s3 = Singleton().__new__(Singleton)
    print(s1 is s3)           # True — mesmo tentando forçar, retorna a mesma instância
```

**Por que é mais robusto que `get_instance()`?**

No `singleton1_1.py`, chamar `ConfigSingleton()` diretamente **burla** o padrão — cria uma nova instância.  
Aqui, `__new__` é chamado **antes** de `__init__` em toda instanciação. O controle está na criação do objeto em si, não num método auxiliar.

| | `get_instance()` | `__new__` |
|---|---|---|
| `Classe()` direto | ❌ burla o singleton | ✅ respeita |
| `Classe.__new__(Classe)` direto | ❌ burla | ✅ respeita |
| Precisa lembrar de chamar método especial | Sim | Não |

**Por que `super().__new__(cls)`?**

`super()` chama o `__new__` de `object` (classe base de tudo em Python), que é quem realmente aloca o objeto na memória. Sem isso, o objeto não seria criado.

> Transparente para quem usa — instancia normalmente com `Singleton()`.

---

#### Forma 3 — Thread-safe com locking

Necessário quando múltiplas threads podem criar instâncias simultaneamente.

```python
from threading import Lock

class Singleton:
    _instancia = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instancia is None:
                print("Criando a instância única")
                cls._instancia = super().__new__(cls)
        return cls._instancia
```

> O `Lock` garante que apenas uma thread execute o bloco `if` por vez.  
> Versão mais robusta para aplicações concorrentes.

---

#### Forma 4 — Módulo como Singleton (pythônico)

Python executa o módulo **uma única vez** e cacheia. Toda importação subsequente reutiliza o mesmo objeto sem nenhum código extra.

```python
# config_singleton.py
import json

dados = None

with open("config.json", "r") as arquivo:
    dados = json.load(arquivo)
```

```python
# uso em qualquer arquivo
from config_singleton import dados
print(dados)
# {'database': {'host': 'localhost', 'port': 5432, 'user': 'admin', 'password': 'secret'}}
```

> Forma mais simples e idiomática em Python. Não precisa de classe.

---

#### Comparativo

| Forma | Linguagem-friendly | Thread-safe | Pythônico |
|---|---|---|---|
| `get_instance()` | Java/C++ | Não (sem lock) | Não |
| `__new__` | Python | Não | Parcialmente |
| Lock | Python | **Sim** | Parcialmente |
| Módulo | Python | **Sim** (GIL) | **Sim** |

---
