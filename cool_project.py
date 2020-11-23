import re   
print("enter file name")
counter = dict()
listy = list()
x = raw_input()
y = open(x)
readed = y.read()
letter = re.findall('[a-z]',readed)
sorty = sorted(letter)
for i in sorty:
    counter[i] = counter.get(i, 0 ) + 1    
for k, v in counter.items():
    listy.append( (v,k) )
listy = sorted(listy, reverse=True)
for v,k in listy:
    print( (k,v))