
def add(x, y):

    c= x + y
    return c


def subtract(x, y):
    d= x - y
    return d


def multiply(x, y):
    e= x * y
    return e


def divide(x, y):
    f= x / y
    return f

ch = raw_input("enter start to perform calculations: ")
while ch == "start":
    x = int(input("enter first number:"))
    y = int(input("enter second number:"))
    print ("select operations to perform:")
    print("1-ADDITION")
    print("2-SUBTRACTION")
    print("3-MULTIPLICATION")
    print("4-DIVISION")
    choice = input("Enter choice(1/2/3/4): ")
    if choice in (1, 2, 3, 4):
        if choice == 1:
            print(x, "+", y, "=",add(x, y))
        elif choice == 2:
            print(x, "-", y, "=",subtract(x, y))
        elif choice == 3:
            print(x, "*", y, "=",multiply(x, y))
        elif choice == 4:
            print(x, "/", y, "=", divide(x, y))
        else:
            print("Invalid input")
        
        next_variable = raw_input("Let's do next calculation? (yes/no): ")
        if next_variable == "no":
            break
        else:

            ch = raw_input("enter start to perform calculations:")

