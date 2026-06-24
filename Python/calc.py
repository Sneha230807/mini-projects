def calculator():
    print("--- Simple Python Calculator ---")
    while True:
        print("\n1.Add 2.Sub 3.Mul 4.Div 5.Exit")
        choice = input("Choice (1-5): ")
        if choice == '5': break
        if choice in ('1', '2', '3', '4'):
            try:
                n1, n2 = float(input("Num1: ")), float(input("Num2: "))
                if choice == '1': print("Result:", n1 + n2)
                elif choice == '2': print("Result:", n1 - n2)
                elif choice == '3': print("Result:", n1 * n2)
                elif choice == '4':
                    print("Result:", n1 / n2 if n2 != 0 else "Error: Div by 0")
            except ValueError: print("Invalid Input")
        else: print("Invalid Choice")

if __name__ == "__main__": calculator()
