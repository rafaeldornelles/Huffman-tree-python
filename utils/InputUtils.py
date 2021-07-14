from typing import List


class InputUtils:
    # Faz uma pergunta cuja resposta seja sim ou nao e retorna um boleano
    @staticmethod
    def questionYesNo(question) -> bool:
        while True:
            answer = input(question + "(s/n): ")
            if answer in ["s","S","sim","Sim", "SIM"]:
                return True
            elif answer in ["n", "N", "nao", "Nao", "não", "Não", "NAO", "NÃO"]:
                return False
            else:
                print("Valor inválido.")

    # Pergunta se o usuário quer fazer outra operaçao e retorna True ou False
    @staticmethod
    def wantsToContinue()-> bool:
        print('\n\n\n')
        return InputUtils.questionYesNo("Deseja Fazer outra operação?")


    # Lê uma variavel do tipo string (sem numeros e simbolos)
    @staticmethod
    def readString(message: str) -> str:
        def stringValida(string):
            for char in string:
                if not char.isalpha() and char != ' ':
                    return False
            return True


        while True:
            string = input(message)

            if stringValida(string):
                return string
            else:
                print("Valor digitado contém caracteres inválidos")


    # Lê uma variável do tipo inteiro
    @staticmethod
    def readInt(message: str) -> int:
        while True:
            try:
                inteiro = int(input(message))
                return inteiro
            except:
                print("Valor Inválido")

    # Lê uma variável do tipo float
    @staticmethod
    def readFloat(message: str) -> float:
        while True:
            try:
                num = float(input(message))
                return num
            except:
                print("Valor Inválido")


    #converte uma lista de strings em uma tabela
    @staticmethod
    def choiceTable(header: str, data: List, l=50):
        print("-"*l)
        print(header.center(l))
        print("-"*l)
        for i, d in enumerate(data):
            line = "|" + f"{i+1}".center(7) + "-   " + f"{d}".ljust(l-13) + "|"
            print(line)

    #Escolhe uma opção dentre uma lista. Retorna o índice da opção escolhida.
    @staticmethod
    def chooseOption(options: List[str], message="Escolha uma opção: ", l=50):
        while True:
            InputUtils.choiceTable(message, options, l)
            escolha = InputUtils.readInt("\nEscolha: ")
            if escolha - 1 in range(len(options)):
                return escolha - 1
            else:
                print("Valor fora do escopo de opções.")
