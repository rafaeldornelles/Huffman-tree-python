import json


class IoUtils:
    @staticmethod
    def readFile(path: str):
        with open(path, "r", encoding="utf-8") as file:
            return "".join(file.readlines())

    @staticmethod
    def readCompressedFile(path: str):
        with open(path, "r", encoding="utf-8") as file:
            frequencies = json.loads(file.readline())
            textCompressed = file.readline()
            return frequencies, textCompressed

    @staticmethod
    def countFrequencies(string: str):
        freqDict = {}
        for char in string:
            if char in freqDict.keys():
                freqDict[char] +=1
            else:
                freqDict[char] = 1
        return freqDict

    @staticmethod
    def writeFile(path:str, instructions: str, content: str):
        with open(path, "w+", encoding="utf-8") as file:
            file.write(instructions)
            file.write("\n")
            file.write(content)

    @staticmethod
    def writeDecompressedFile(path: str, content:str):
        with open(path, "w+", encoding="utf-8") as file:
            file.write(content)