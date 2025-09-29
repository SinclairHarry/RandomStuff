with open("falseFinderThing/mid.txt") as t:
    text = t.read()
newText = ''
print(''.join(chr(int(''.join(list(map(lambda x: '0' if x[0] == "y" else ("",'1')[x[0]=="x"], text.split("."))))[i:i+7], 2)) for i in range(0,len(''.join(list(map(lambda x: '0' if x[0] == "y" else ("",'1')[x[0]=="x"], text.split("."))))), 7)))