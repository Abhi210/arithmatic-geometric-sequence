#AGM
import math
a= int(input("Enter a0"))
b= int(input("Enter b0"))


la=[a]
lb=[b]

n = int(input("Enter no of iteration"))

def agm(a,b,n):
    for x in range(n):
          a1=(a+b)/2
          b1=math.sqrt(a*b)
          la.append(a1)
          lb.append(b1)
          a,b=a1,b1
          x=x+1
          

    return la,lb

agm(a,b,n)
print(la)
print(lb)
          
          
