marks = int(input("enter the marks : "))

if marks < 0 or marks > 100:
    print("invalid marks")
elif marks >= 90:
    print("grade A")
elif marks >= 50:
    print("grade B")
elif marks >= 33:
    print("grade C")
else:
    print("fail")