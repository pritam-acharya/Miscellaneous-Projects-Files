# factorial gand mara
def fact(num):
    if num == 0:
        return 1
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial*i
    return factorial

listofnum = []
n = int(input("please enter number of numbers:"))
for i in range(1,n+1):
    n1 = int(input("enter the numbers:"))
    listofnum.append(n1)
for x in listofnum:
    xfact = fact(x)
    print(f"the factorial of {x} is {xfact}")