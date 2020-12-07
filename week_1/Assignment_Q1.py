#Define a function to print a string diagonally as well as reversed diagonally

# Forward Diagonally
N= "MUHAMMAD AASHIR KHAN"
for x in range(len(N)):
    print( ' ' * (x), N[x])
print("")
print("")
#Reverse Diagonal
N= "MUHAMMAD AASHIR KHAN"
for x in reversed(range(len(N))):
    print( ' ' * (x), N[x])