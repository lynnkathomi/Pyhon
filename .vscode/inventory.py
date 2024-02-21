# Function to add an item to the inventory
def add_to_inventory(item_name, quantity, inventory):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

# Function to retrieve information about a specific item in the inventory
def get_item_info(item_name, inventory):
    if item_name in inventory:
        return f"{item_name}: {inventory[item_name]}"
    else:
        return f"{item_name} not found in inventory"

# Function to calculate and display the total quantity of all items in the inventory
def get_total_quantity(inventory):
    total_quantity = sum(inventory.values())
    return f"Total quantity: {total_quantity}"

# Main program loop
inventory = {}  # Initialize the inventory as an empty dictionary
while True:
    print("1. Add item to inventory")
    print("2. Get item info")
    print("3. Get total quantity")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        food_name = input("Enter food item name: ")
        quantity = int(input("Enter quantity: "))
        
        add_food_to_inventory(food_name, quantity, inventory)
    elif choice == "2":
        item_name = input("Enter item name: ")
        print(get_item_info(item_name, inventory))
    elif choice == "3":
        print(get_total_quantity(inventory))
    elif choice == "4":
        break
    else:
        print("Invalid choice")
