#from time import perf_counter

#startTime = perf_counter()

#reads lambda encrypted file
with open("falseFinderThing/mid.txt") as t:
    text = t.read()
newText = ''
finalList = []
for char in range(1,len(text)):
    if text[char] == ")":
        if text[char-1] == "y":
            newText +="0"
        else:
            newText += "1"
    elif text[char] == " " or text[char] == "\n":
        newText += " "
for bina in newText.split(" "):
    finalList.append(chr(int(bina,2)))
phrase = ''.join(finalList)
print(phrase)


#finTime = perf_counter()-startTime
#print(finTime)