import pandas

data = pandas.read_csv("npa.csv")
phoneticDict = {row.letter: row.code for (index, row) in data.iterrows()}

def generatePhonetic():
    name = input("Enter a name: \n").upper()
    try:
        outputList = [phoneticDict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generatePhonetic()
    else:
        print(outputList)

generatePhonetic()