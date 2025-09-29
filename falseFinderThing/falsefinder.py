#Converts the lambda calculus expressions for true and false into 1 and 0, respectively
def BinaryConverter(text):
    newText = ''
    for char in range(1,len(text)):
        if text[char] == ")":
            if text[char-1] == "y":
                newText +="0"
            else:
                newText += "1"
    return newText

#separates the string of 1s and 0s into groups of 7
def BinarySeparator(text):
    word = ''
    for i in range(len(text)):
        word += text[i]
        if (i+1)%7 == 0 and i != 0:
            word += " "
    return word

with open("falseFinderThing/mid.txt") as t:
    text = t.read()

print(BinarySeparator(BinaryConverter(text)))