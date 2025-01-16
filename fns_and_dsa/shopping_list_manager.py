


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = input("Enter your choice: ")
            int(choice)
            
        except ValueError:
                print("please enter a valid number")
        
        if choice == '1':
                item_name = input("Item name: ")
                shopping_list.append(item_name)

        elif choice == '2':
            item_name = input("Item name: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
            else:
                print("item does not exist")

        elif choice == '3':
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()