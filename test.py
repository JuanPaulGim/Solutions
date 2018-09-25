L = ""
for i in range(1000000):
 if(i>=999997):
  L += str(i+1) + " "
 else:
  L += str(i) + " "
L = L.strip(" ")
print (L)