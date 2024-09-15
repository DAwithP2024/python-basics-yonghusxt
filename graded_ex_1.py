import re
# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == 1:
        sorted_products = sorted(products_list, key=lambda x: x[1])
    elif sort_order == 2:
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    return sorted_products


def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        name, price = product
        print(f"{index}. {name}: {price}")


def display_categories():
    categories = list(products.keys())
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    name, price = product
    new_product = (name, price, quantity)
    cart.append(new_product)

def display_cart(cart):
    total=0
    for index, product in enumerate(cart, start=1):
        name, price,quantity = product
        print(f"{index}. {name} - price:{price} quantity:{quantity}")
        total=total+price*quantity
    return total


def generate_receipt(name, email, cart, total_cost, address):
    print("Name:", name)
    print("Email:", email)
    print("Items Purchased:")
    display_cart(cart)
    print("Total Cost: $", total_cost)
    print("Delivery Address:", address)
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    names = name.split()
    if len(names) != 2:
        print("The name must include both the first name and the last name. Please enter a valid name.")
        return False
    for letter in names:
        if not letter.isalpha():
            print("The name must consist entirely of letters, please enter a valid name again.")
            return False
    return True

def validate_email(email):
    email_pattern = r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$"
    ret = re.match(email_pattern, email)
    if not ret:
        print("Please enter a correctly formatted email address.")
        return False
    return True

def while_number():
    display_categories()
    while True:
        number=input("Please enter the category number you want to explore: ")
        number=int(number)
        product_name="IT Products"
        if number==1:
           print(f"\nProducts in IT Products:")
           display_products(products["IT Products"])
           break
        elif number==2:
           print(f"\nProducts in Electronics:")
           display_products(products["Electronics"])
           product_name="Electronics"
           break
        elif number==3:
           print(f"\nProducts in Groceries:")
           display_products(products["Groceries"])
           product_name="Groceries"
           break
        else:
           print("Please enter the correct number.")
           continue
    return product_name
    
def main():
    cart = list()
    check1 = False
    while not check1:
        name = input("Please provide your first name and last name, and these names should only contain letters:")
        check1 = validate_name(name)
    check2 = False
    while not check2:
        email = input("Please input your email:")
        check2 = validate_email(email)
    address = input("Please input your address:")
    print()
    product_name = while_number()
    while True:
        print(f"\n1. Select a product to buy")
        print("2. Sort the products according to the price. ")
        print("3. Go back to the category selection.")
        print(f"4. Finish shopping\n")
        choice = input("Please enter your choice:")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                check3 = False
                while not check3:
                    check4 = False
                    product_number = input("Please enter the product number you want to purchase:")
                    if product_number.isdigit():
                        product_number = int(product_number)
                        for index, product in enumerate(products[product_name], start=1):
                            if product_number == index:
                                new_product1 = product
                                check4=True
                                break
                    else:
                        print("Please enter a product number.")
                        continue
                    if check4 == False:
                        print("Please enter the correct product number.")
                        continue
                    else:
                        check3 = True
                check5 = False
                while not check5:
                    quantity = input("Please enter the quantity you want to purchase:")
                    if quantity.isdigit():
                        quantity = int(quantity)
                        check5 = True
                    else:
                        print("Please enter a number.")
                add_to_cart(cart, new_product1, quantity)
                continue
            elif choice == 2:
                while True:
                    sort_order = input("Enter 1 for ascending order or 2 for descending order: ")
                    if sort_order.isdigit():
                         sort_order=int(sort_order)
                         products[product_name]=display_sorted_products(products[product_name], sort_order)
                         display_products(products[product_name])
                         break
                    else:
                        print("Please enter 1 or 2")
                        continue
                continue
            elif choice == 3:
                product_name = while_number()
                continue
            elif choice == 4:
                if len(cart)>0:
                    total=display_cart(cart)
                    print("Total Cost: $", total)
                    print()
                    print("---------------------------------------------")
                    print("Receipt:")
                    generate_receipt(name, email, cart, total, address)
                    print("---------------------------------------------")
                    break
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day")
                    break
            else:
                print("Please input the correct choice.")
        else:
             print("Please input the correct choice.")
             continue
    

        
""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
