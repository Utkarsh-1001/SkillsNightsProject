print(".....QUADRATIC EQUATION SOLVER.....")
while True:
    print("For a quadratic equation:")
    print("\t ax^2 + bx + c = 0 ,")

    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    c = float(input("Enter c:"))

    D = (b**2.0)-(4.0)*(a*c)

    if D>=0:
        x1= (-b + ((D)**0.5))/(2.0*a)
        x2= (-b -((D)**0.5))/(2.0*a)
        print("The real values of x are:")
        print(f"x1=",x1)
        print(f"x2=", x2)
    else:
        f = ((-D)**0.5)
        print("The imaginary values of x are:")
        print('x1=',(-b)/2.0, '+ i',(f)/2.0)
        print('x2=',(-b)/2.0, '- i',(f)/2.0)
    a = input("Enter \'n\' to quit and any other key to continue:\n")[0]
    if (a == "n"):
        break
       