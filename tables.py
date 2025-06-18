def table (n):
    def series (i=1):
        if i<=10:
            print(f"{n}*{i} =",n*i)
            return series (i+1)
    return series()

def s(n):
    if n==0:
        return 0
    elif n>=1:
        return n+s(n-1)


# table(15)

print(s(100))



