import string 

class Alphabet:
    def __init__(self, lenga, lettera):
        self.letters = list(lettera)
        self.leng = lenga

    def printLetter(self):
        print(self.letters)

    def _LetterNum(self):
        len(self.letters)

class EngAlphabet(Alphabet):

    _alphabetLeng = 26 # Static alphabet length

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter in self.letters:
            return True
        return False
    
    def LetterNum(self):
        return EngAlphabet._alphabetLeng


    @staticmethod
    def example():
        print("This is an example letter")

def __main__():
    eng = EngAlphabet()
    eng.printLetter()
    print(eng.is_en_letter("Щ"))
    print(eng.is_en_letter("F"))
    print(eng.LetterNum())
    eng.example()

if __name__ == "__main__":
    __main__()