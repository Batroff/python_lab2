# БСБО-05-19 Савранский Сергей


class Brother:

    def __init__(self, a: dict):
        self._abilities = a.copy()

    @property
    def abilities(self) -> dict:
        return self._abilities

    def train(self, ability_index: int, ability_incr: int) -> None:
        self._abilities[ability_index] += ability_incr

    def print_abilities(self) -> None:
        print(' '.join(str(val) for val in self._abilities.values()))

    def count_equal_abilities(self, a: dict) -> int:
        ctr = 0
        for i in range(len(self._abilities)):
            if self._abilities[i] == a[i]:
                ctr += 1
        return ctr


abilities = {i: int(input()) for i in range(int(input('S >> ')))}

brothers = {
    1: Brother(abilities),
    2: Brother(abilities)
}

for i in range(int(input('N >> '))):
    brother_index = int(input('Brother # >> '))

    brothers[brother_index].train(int(input('Ability >> ')), int(input('Increment >> ')))

for brother in brothers.values():
    brother.print_abilities()
print(brothers[1].count_equal_abilities(brothers[2].abilities))
