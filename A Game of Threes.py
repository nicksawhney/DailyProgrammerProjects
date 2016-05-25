user_number = int(input("What's your ungodly big number? "))


def three_sum(n):
    while n!= 1:
        if n % 3 == 0:
            print (int(n) , "0")
            n = n/3
        elif n % 3 == 1:
            print (int(n) , "-1")
            n = (n-1)/3
        else:
            print (int(n) , ("+1"))
            n = (n+1)/3
    print (1)
print (three_sum(user_number))
