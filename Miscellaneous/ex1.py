def AM(melist):
    sum = 0
    for num in melist:
        sum = sum+num
        AM = sum/len(melist)
    return AM
def GM(melist):
    product = 1
    for num in melist:
        product = product*num
        GM = (product)**(1/len(melist))
    return GM

melist = []
n = int(input("Please enter the number of entires:"))
for i in range(0, n):
    x = int(input("Please enter the numbers:"))
    melist.append(x)
for b in melist:
    ArMe = AM(melist)
    GeMe = GM(melist)
print(f"the arithmetic mean is {ArMe:.3f} and the geometric mean is {GeMe:.3f}")