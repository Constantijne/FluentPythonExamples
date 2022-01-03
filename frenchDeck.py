import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


def __doc__():
    return ''' Программа-пример с колодой карт '''


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


print(__doc__())

firstDeck = FrenchDeck()
print(len(firstDeck))

for i in range(len(firstDeck)):
    print(firstDeck[i])
