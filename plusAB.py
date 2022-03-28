def F(n):
    if n!=0:
        return F(n-1)*n
    else: return 1
print(F(3))
