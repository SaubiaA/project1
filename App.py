
def calculator():
    A = int(input("Enter the value of a: "))
    B = int(input("Enter the value of b: "))
    operator = input("Enter operator: ")
    if operator == 'S':
        print(A-B)
    elif operator == 'A':
        print(A+B)
    elif operator == 'D':
        print(A/B)
    elif operator == 'M':
        print(A*B)
    elif operator == 'P':
        print(A%B)
    else:
        print("\nError: incorrect operator\n")


def main():
    print("Hello World!")
    calculator()
    print("Opertion completed")



if __name__ == "__main__":
    main()