import collections
text = open("Engl.txt")
f1 = text.read()
l = f1.lower()
l = f1.split()
L1 = collections.Counter(l)
print(L1)