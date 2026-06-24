def main():
    tasks = []
    while True:
        print("\n1. View\n2. Add\n3. Delete\n4. Exit")
        choice = input("Enter (1-4): ")
        if choice == "1":
            print("\n".join([f"{i+1}. {t}" for i, t in enumerate(tasks)]) or "Empty")
        elif choice == "2":
            tasks.append(input("Task: "))
        elif choice == "3":
            try:
                tasks.pop(int(input("Delete #: ")) - 1)
            except (ValueError, IndexError):
                print("Invalid number")
        elif choice == "4": break

if __name__ == "__main__":
    main()
