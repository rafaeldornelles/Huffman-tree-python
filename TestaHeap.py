from Huffman import Huffman
from IoUtils import IoUtils

strtest = IoUtils.readFile('teste.txt')

huffman = Huffman.forCompression(strtest)
IoUtils.writeFile('output.txt', huffman.translationJson, huffman.compress())

frequencies, compressed = IoUtils.readCompressedFile("output.txt")

decompressionHuffman = Huffman.forDecompression(frequencies)
IoUtils.writeDecompressedFile("output-decompressed.txt", decompressionHuffman.decompress(compressed))