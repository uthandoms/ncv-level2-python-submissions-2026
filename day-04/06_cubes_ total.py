
total = 0
n = int(input("Please enter number:"))
for x in range(1,n+1):
    cube = x**3
    print(cube, end=",")
    total = total + cube
    