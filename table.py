def table (n):
    def series (i=1):
        if i<=10:
            print(f"{n}*{i} =",n*i)
            return series (i+1)

table(10)

