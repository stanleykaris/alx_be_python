shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def add_items():
    item = input("Enter an item to add to the shopping list: ").strip()
    if item:
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
    else:
        print("Item cannot be empty.")
        
def remove_item():
    if not shopping_list:
        print("The shopping list is empty. Nothing to remove.")
        return
    
    item = input("Enter an item to remove from the shopping list: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"\n{item} has been removed from the shopping list.")
    else:
        print(f"\n{item} is not in the shopping list.")
        
def view_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
            
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            add_items()
            pass
        elif choice == '2':
            remove_item()
            pass
        elif choice == '3':
            view_list()
            pass
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            break
            
if __name__ == '__main__':
    main()