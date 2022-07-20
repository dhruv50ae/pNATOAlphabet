import pandas

data = pandas.read_csv("npa.csv")
phoneticDict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phoneticDict)
name = input("Enter a name: \n").upper()
outputList = [phoneticDict[letter] for letter in name]

print(outputList)