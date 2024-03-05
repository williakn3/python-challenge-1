# Menu Dictionary

menu_items = {
   1:  {"Item_name": "Chili Cheese Fries", "Price": 5.99},
   2:  {"Item_name": "Cheese Sticks", "Price": 7.99},
   3:  {"Item_name": "Spinach Dip", "Price": 9.99},
   4:  {"Item_name": "Steak Bites", "Price": 12.99},
   5:  {"Item_name": "Chicken Alfredo","Price": 16.99},
   6:  {"Item_name": "Chicken Piccata", "Price": 17.99},
   7:  {"Item_name": "Lasagna", "Price": 19.99},
   8:  {"Item_name": "Chicken Carbonara", "Price": 22.99},
        
    }

customer_order = [] 


def print_menu(menu_items):
    print("what can i get you started with today? ")
    for key, value in menu_items.items():
        print(f"{key}: {value['Item_name']} - ${value['Price']}")    


#take order
def take_order():
    place_order = True
    while True:
        print_menu(menu_items)
        menu_selection = input("Enter your order here (type 'done' to finish): ")
        #check if user entered 'done'

    

        if menu_selection.lower() =='done':
            break

        if not menu_selection.isdigit() or int(menu_selection) not in menu_items:
            print("Error: Please enter a valid number.")
            continue
        menu_selection = int(menu_selection)   #convert to integer

        #check if selection is in menu
        
        quantity = input(f"how many of {menu_items[menu_selection]['Item_name']} do you want to order? ")

        if not quantity.isdigit():
            print ("Error: please enter a valid quantity. Defaulting to 1. ")
            quantity = 1
        else:
             quantity = int(quantity)



           # Append the customer's order to the order list in dictionary format 
        customer_order.append({
            "Item_name": menu_items[menu_selection]["Item_name"],
            "Price": menu_items[menu_selection]["Price"],
            "Quantity": quantity




    })

    #check if they would like anything else

    add_more = input("Is there anything else I can get for you? (yes/no): ")

    match add_more.lower():
        case 'y':
            place_order = True
        case 'n':
            place_order = False
            print("Thank you for your Order!")
        case _:
            print("Invalid input. Please try again.")

    
        
#Print Receipt
def print_receipt(order):
    print("\nYour order receipt:")
    for item in customer_order:
        item_name = item['Item_name']
        price = "${:.2f}".format(item['Price'])
        quantity = item['Quantity']
        print("{:<30} | {:<10} | {:<10}".format(item_name, price, quantity))
        print("_" * 54)
        
    total_price = sum(item['Price'] * item['Quantity'] for item in customer_order)
    print(f"Total price: ${total_price: .2f}")

 #Run Program
def main():
    take_order()
    print_receipt(customer_order)

if __name__ == "__main__":
    main()
