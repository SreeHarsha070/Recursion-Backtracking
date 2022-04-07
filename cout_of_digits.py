def summ(n,c):
    if n==0:
        return c
    return summ(n//10,c+1)
n=int(input())
print(summ(n,0))


