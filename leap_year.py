y = int(input())

if y%4 ==0:
    if y%400 ==0 or y%100 != 0:
        print ("{} is a leap year".format(y))
    else:
        print ("{} is a non leap year".format(y))
else:
    print ("{} is a non leap year".format(y))
    
