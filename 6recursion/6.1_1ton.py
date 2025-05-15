def print1ToN(n):
    if n > 0:
        print1ToN(n - 1)
        print(n, end=' ')
        
def printNto1(n):
    if n > 0:
        print(n, end=' ')
        printNto1(n - 1)

n = int(input("Enter Input : "))
if n <= 0 :
    n=1
print1ToN(n)
printNto1(n)