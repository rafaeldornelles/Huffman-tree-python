import json
from typing import Dict

from Heap import Heap
from utils.IoUtils import IoUtils
from Nodo import Nodo


class Huffman:
    @classmethod
    def forCompression(cls, textToCompress: str):
        huffmann = cls()
        huffmann.textToCompress = textToCompress
        frequencies = IoUtils.countFrequencies(textToCompress)
        frequenciesNodeList = [Nodo(item[1], item[0]) for item in frequencies.items()]
        huffmann._translationJson = json.dumps(frequencies)
        huffmann._frequenciesHeap = Heap.heapify(frequenciesNodeList)
        huffmann.parentNode = huffmann._heapMergeIteraction()
        huffmann._keysDictionary = {}
        huffmann._setKeysDictionary(huffmann.parentNode)
        return huffmann

    @classmethod
    def forDecompression(cls, frequencies: Dict):
        huffmann = cls()
        frequenciesNodeList = [Nodo(item[1], item[0]) for item in frequencies.items()]
        huffmann._frequenciesHeap = Heap.heapify(frequenciesNodeList)
        huffmann.parentNode = huffmann._heapMergeIteraction()
        return huffmann

    @property
    def textToCompress(self):
        return self._textToCompress

    @textToCompress.setter
    def textToCompress(self, text):
        self._textToCompress = text

    @property
    def parentNode(self):
        return self._parentNode

    @parentNode.setter
    def parentNode(self, parentNode: Nodo):
        self._parentNode = parentNode

    @property
    def translationJson(self):
        return self._translationJson

    @translationJson.setter
    def translationJson(self, translationJson):
        self._translationJson = translationJson

    def _heapMergeIteraction(self)-> Nodo:
        if self._frequenciesHeap.size == 1: return self._frequenciesHeap.extractMin()
        valA = self._frequenciesHeap.extractMin()
        valB = self._frequenciesHeap.extractMin()
        mergeNode = Nodo(valA.frequency + valB.frequency, None)
        mergeNode.left = valA
        mergeNode.right = valB
        self._frequenciesHeap.insert(mergeNode)
        return self._heapMergeIteraction()

    #Iterar pela árvore até encontrar a folha do caractere.
    def _setKeysDictionary(self, nodo: Nodo, key:str = ""):
        if nodo.isLeaf():
            self._keysDictionary[nodo.character] = key
            return
        self._setKeysDictionary(nodo.left, key + "0")
        self._setKeysDictionary(nodo.right, key + "1")

    def _findCharBykey(self, nodo: Nodo, key:str):
        if len(key) == 0: return nodo.character
        keyBit = key[0]
        key = key[1:]
        nodoToVisit = nodo.left if keyBit == "0" else nodo.right
        return self._findCharBykey(nodoToVisit, key)

    def compress(self):
        output = ""
        for char in self.textToCompress:
            output += self._keysDictionary[char]
            output += " "
        return output

    def decompress(self, compressed: str):
        keys = compressed.strip().split(" ")
        output = ""
        for key in keys:
            output += self._findCharBykey(self.parentNode, key)
        return output

