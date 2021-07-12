from typing import Optional


class Nodo:
    def __init__(self, frequency: int, character:Optional[str]):
        self.left = None
        self.right = None
        self.frequency = frequency
        self.character = character

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node: 'Nodo'):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, frequency: int):
        self._right = frequency

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: int):
        self._frequency = frequency

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character: str):
        self._character = character


    def isEmpty(self):
        return self.left is None and self.right is None and self.frequency is None and self.character is None

    def __str__(self):
        return fr"{self.character}: {self.frequency}"

    def isLeaf(self):
        a = self.isEmpty()
        return not self.isEmpty() and self.left is None and self.right is None