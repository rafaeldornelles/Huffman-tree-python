# Material consultado : https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
from typing import Optional, List

from Nodo import Nodo


class Heap:
    def __init__(self):
        self.heapList = [None]  # Iniciando a lista com valor nulo para facilitar calculos de obtenção dos indices parent e children
        self.size = 0

    @property
    def heapList(self) -> List[Nodo]:
        return self._heapList

    @heapList.setter
    def heapList(self, heapList: List[Nodo]):
        self._heapList = heapList

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int):
        self._size = size

    def _getNode(self, index):
        if index > self.size or index <= 0: return None
        return self.heapList[index]

    def _getLeftChild(self, index):
        return self._getNode(index * 2)

    def _getRightChild(self, index):
        return self._getNode(index * 2 + 1)

    def _getParent(self, index):
        return self._getNode(self._getParentIndex(index))

    def _getParentIndex(self, index):
        return index // 2

    def insert(self, nodo: Nodo):
        self.heapList.append(nodo)
        self.size += 1
        self._percUp(self.size)

    def _percUp(self, index):
        node = self._getNode(index)
        parent = self._getParent(index)
        parentIndex = self._getParentIndex(index)
        if parent is None or node.frequency >= parent.frequency: return
        self._swap(index, parentIndex)
        self._percUp(parentIndex)

    def _percDown(self, index):
        node = self._getNode(index)
        minChild = self.getMinChild(index)
        minChildIndex = self._getMinChildIndex(index)
        if minChild is None or node.frequency <= minChild.frequency: return
        self._swap(index, minChildIndex)
        self._percDown(minChildIndex)

    def _swap(self, indexA, indexB):
        if max(indexA, indexB) > self.size or min(indexA, indexB) <= 0: return
        self.heapList[indexA], self.heapList[indexB] = self.heapList[indexB], self.heapList[indexA]

    def _getMinChildIndex(self, index):
        if self._isLeaf(index):
            return None
        elif self._hasOnlyOneChild(index):
            return index * 2
        leftChild = self._getLeftChild(index)
        rightChild = self._getRightChild(index)
        return index * 2 if min(leftChild.frequency, rightChild.frequency) == leftChild.frequency else index * 2 + 1

    def getMinChild(self, index):
        minChildIndex = self._getMinChildIndex(index)
        if minChildIndex is None: return None
        return self._getNode(minChildIndex)

    def _isLeaf(self, index):
        return index * 2 > self.size

    def _hasOnlyOneChild(self, index):
        return index * 2 == self.size

    def extractMin(self) -> Optional[Nodo]:
        if self.size == 0: return None
        returnVal = self.heapList[1]
        lastVal = self.heapList.pop()
        if self.size > 1:
            self.heapList[1] = lastVal
        self.size -= 1
        self._percDown(1)

        return returnVal

    @staticmethod
    def heapify(list):
        heap = Heap()
        heap.heapList += list
        heap.size = len(list)
        i = len(list) // 2
        while i > 0:
            heap._percDown(i)
            i -= 1
        return heap

    def printList(self):
        print(", ".join([str(i) for i in self.heapList]))
