from Huffman import Huffman
from utils.InputUtils import InputUtils
from utils.IoUtils import IoUtils

class Main:
    @staticmethod
    def showMenuPrincipal():
        while True:
            opcoes = ["Comprimir Arquivo", "Descomprimir Arquivo"]
            escolha = InputUtils.chooseOption(opcoes, "Bem vindo! Escolha a opção desejada")
            if escolha == 0:
                Main.compression()
            else:
                Main.decompression()
            if not InputUtils.wantsToContinue(): return


    @staticmethod
    def compression():
        defaultPath = "teste.txt"
        defaultOutputPath = "output.txt"
        path = InputUtils.readString("Insira o nome do arquivo que será lido na pasta atual: (teste.txt) ")
        content = IoUtils.readFile(path or defaultPath)
        huffman = Huffman.forCompression(content)
        outputPath = InputUtils.readString("Insira o nome do arquivo comprimido a ser gravado: (output.txt) ")
        compressed = huffman.compress()
        IoUtils.writeFile(outputPath or defaultOutputPath, huffman.translationJson, compressed)
        print()
        print(f"Arquivo comprimido com sucesso. Arquivo Gerado: {outputPath or defaultOutputPath}")
        print(f"Tamanho original do texto ASCII: {len(content) * 8} bits")
        print(f"Tamanho comprimido do texto: {len(compressed)} bits")
        print(f"Compressão: {round((1 - len(compressed) / (len(content)*8)) * 100)}%")


    @staticmethod
    def decompression():
        while True:
            defaultPath = "output.txt"
            defaultOutputPath = "output-decompressed.txt"
            path = InputUtils.readString("Insira o nome do arquivo comprimido que será lido na pasta atual: (output.txt) ")
            frequencies, compressed = IoUtils.readCompressedFile(path or defaultPath)
            if frequencies == compressed == None:
                print("Formato de arquivo Inválido. Indique um arquivo que já tenha sido comprimido.")
                continue
            huffman = Huffman.forDecompression(frequencies)
            outputPath = InputUtils.readString("Insira o nome do arquivo comprimido a ser gravado: (output-decompressed.txt) ")
            IoUtils.writeDecompressedFile(outputPath or defaultOutputPath, huffman.decompress(compressed))
            print("Arquivo descomprimido com sucesso.")
            return

Main.showMenuPrincipal()
