i = float(input("please enter a number less than 100:"))
if i > 100:
    print("chutiya mat bana")
else:
    while i < 100:
        if i % 2 == 0:
            i = i+2
            print(f"the following even number less than 100 is:{i}")
            if i > 100: break
        else:
            i = i+2
            print(f"the following odd number less than 100 is: {i}")
            if i > 100: break



