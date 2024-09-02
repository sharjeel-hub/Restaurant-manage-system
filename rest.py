menu = {}

def add_items():
    name = input("Enter item's Name: ")
    price = float(input("Enter Price: "))
    quantity = input("Number of Items: ")
    extra = input("Any Suggestion or tips of your order: ")
    menu[name] = {"price": price, "quantity": quantity, "suggestion": extra }

def remove_items():
    name = input("Item names: ")
    if name in menu:
        del menu[name]
        print(f"Item '{name}' removed from menu: ")
    else:
        print(f" Item '{name}' not found!")

def display_menu():
    print("Current menu")
    for item, details in menu.items():
        print(f"{item} : ${details['price']:.2f}")

def list_menu():
    print("Here is our current menu:")
    for item in menu.keys():
        print(item)

def main():
    menu["kabab"] = {"price": 89.00, "quantity": "", "suggestion": ""}
    menu["chicken"] = {"price": 99.00, "quantity": "", "suggestion": ""}
    menu["pulao"] = {"price": 69.00, "quantity": "", "suggestion": ""}
    menu["biryani"] = {"price": 79.00, "quantity": "", "suggestion": ""}
    menu["kofty"] = {"price": 99.00, "quantity": "", "suggestion": ""}
    menu["drinks"] = {"price": 89.00, "quantity": "", "suggestion": ""}
    menu["beef"] = {"price": 89.00, "quantity": "", "suggestion": ""}
    menu["Daal Chany"] = {"price": 89.00, "quantity": "", "suggestion": ""}
    menu["sabzi"] = {"price": 89.00, "quantity": "", "suggestion": ""}
    menu["gulab-jamun"] = {"price": 89.00, "quantity": "", "suggestion": ""}

    print("Welcome to SP restaurant!")
    print("Here is our current menu:")
    list_menu()

    while True:
        print("\nRestaurant Management System")
        print("1. Add item to menu")
        print("2. Remove item from menu")
        print("3. Display menu")
        print("4. List menu items")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_items()
        elif choice == "2":
            remove_items()
        elif choice == "3":
            display_menu()
        elif choice == "4":
            list_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()