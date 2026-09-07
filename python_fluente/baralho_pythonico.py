import collections

"""
Módulo de implementação de um baralho de cartas usando collections.namedtuple.
Este módulo demonstra o uso eficiente de collections.namedtuple para criar
estruturas de dados imutáveis e leves. O namedtuple é uma subclasse de tuple
que permite acessar campos por nome em vez de índice, tornando o código mais
legível e pythônico.
Classes:
    Baralho: Representa um baralho completo de 52 cartas.
    Card: namedtuple que representa uma carta individual com suits e rank.
Exemplo de uso:
    >>> baralho = Baralho()
    >>> len(baralho)
    52
    >>> baralho[0]
    Card(suits='spades', rank='2')
Nota sobre collections.namedtuple:
    - Fornece acesso por nome aos elementos (ex: card.suits, card.rank)
    - É imutável, garantindo integridade dos dados
    - Ocupa menos memória que uma classe regular
    - Suporta todas as operações de tupla (indexação, unpacking, etc.)
    - Ideal para estruturas de dados simples sem comportamento complexo
"""


Card = collections.namedtuple("Card", ["rank", "suit"])


class Deck:
    rank = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.Cards = [Card(rank, suit) for suit in self.suits for rank in self.rank]

    def __len__(self):
        return len(self.Cards)

    def __getitem__(self, pos):
        return self.Cards[pos]


if __name__ == "__main__":

    # Imprimindo rankes e suitss disponíveis
    print("rankes disponíveis:", Deck.rank)
    print("suitss disponíveis:", Deck.suits)
    print()

    # Criando uma Card
    beer_card = Card("7", "diamonds")
    print(beer_card)
    print(f"suits: {beer_card.suit}, rank: {beer_card.rank}")

    # Criando e usando o baralho
    deck = Deck()
    print(f"\nTotal de Cards: {len(deck)}")
    print(f"Primeira Card: {deck[0]}")
    print(f"Última Card: {deck[-1]}")

    # Pegando 3 Cards aleatórias
    from random import choice

    print(f"\nCard aleatória: {choice(deck)}")

    # Fatiando o deck
    print(f"\nPrimeiras 3 Cards: {deck[:3]}")
    print(f"\nCards começando do índice 12, pulando 13 cartas: {deck[12::13]}")

    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)

    print(Card("Q", "hearts") in deck)

    print(Card("7", "beasts") in deck)

    print()

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = Deck.rank.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)
