# Material consultado : https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html

class Heap:
    def __init__(self):
        self.heapList = [0] #Iniciando a lista com 0 para facilitar calculos de obtenção dos indices parent e children
        self.size = 0

    def getLeftChild(self, index):
        return  self.getNode(index * 2)

    def getRightChild(self, index):
        return self.getNode(index * 2 + 1)

    def getParent(self, index):
        return self.getNode(self.getParentIndex(index))

    def getParentIndex(self, index):
        return index // 2

    def getNode(self, index):
        if index > self.size or index <= 0: return None
        return self.heapList[index]

    def insert(self, value):
        self.heapList.append(value)
        self.size += 1
        self.percUp(self.size)

    def percUp(self, index):
        node = self.getNode(index)
        parent = self.getParent(index)
        parentIndex = self.getParentIndex(index)
        if parent is None or node >= parent: return
        self.swap(index, parentIndex)
        self.percUp(parentIndex)

    def swap(self, indexA, indexB):
        if max(indexA, indexB) > self.size or min(indexA, indexB) <= 0: return
        self.heapList[indexA], self.heapList[indexB] = self.heapList[indexB], self.heapList[indexA]

    def percDown(self, index):
        node = self.getNode(index)
        minChild = self.getMinChild(index)
        minChildIndex = self.getMinChildIndex(index)
        if minChild is None or node <= minChild: return
        self.swap(index, minChildIndex)
        self.percDown(minChildIndex)


    def getMinChildIndex(self, index):
        if self.isLeaf(index): return None
        elif self.hasOnlyOneChild(index): return index * 2
        leftChild = self.getLeftChild(index)
        rightChild = self.getRightChild(index)
        return index * 2 if min(leftChild, rightChild) == leftChild else index * 2 + 1

    def getMinChild(self, index):
        minChildIndex = self.getMinChildIndex(index)
        if minChildIndex is None: return None
        return self.getNode(minChildIndex)

    def isLeaf(self, index):
        return index*2 > self.size

    def hasOnlyOneChild(self, index):
        return index*2 == self.size


    def extractMin(self):
        if self.size == 0: return None
        returnVal = self.heapList[1]
        lastVal = self.heapList.pop()
        if self.size > 1:
            self.heapList[1] = lastVal
        self.size -=1
        self.percDown(1)

        return returnVal

    def heapify(self, list):
        self.heapList = [0] + list
        self.size = len(list)
        i = len(list) // 2
        while i > 0:
            self.percDown(i)
            i -= 1


    def printList(self):
        print(", ".join([str(i) for i in self.heapList]))
