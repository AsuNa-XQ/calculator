def F(n):
    if n!=0:
        return F(n-1)*n
    else: return 1
print(F(3))

def str(s):
    return s[len(s)-1]+s[1:len(s)-1]+s[0]

def summa(a , b):
    return a+b

def mult(a, b):
    return a*b

a = 5
b = 10
s = "1234"
print(F(a))
print(str(s))
print(summa(a, b))
print(mult(a, b))

