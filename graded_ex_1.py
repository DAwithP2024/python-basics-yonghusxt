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
    pass


def display_products(products_list):
    pass


def display_categories():
    categories = list(products.keys())
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    pass

def display_cart(cart):
    pass


def generate_receipt(name, email, cart, total_cost, address):
    pass


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

def main():
    check1=False
    while not check1:
        name = input("Please provide your first name and last name, and these names should only contain letters:")
        check1=validate_name(name)
    check2=False
    while not check2:
        email=input("Please input your email")
        check2=validate_email(email)
    display_categories()
    number=input("Please enter the category number you want to explore")
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
