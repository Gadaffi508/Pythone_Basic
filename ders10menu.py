def entrance():
    menu = """
        1 - customer transactions
        2 - product processing
        3 - stock transactions
        4 - sales transactions
        5 - exit
    """
    print(menu)
    selection = int(input("please select a transaction : \n"))
    return selection

def customer():
    menu = """
        1 - List customers
        2 - Add new customer
        3 - Update customer
        4 - Delete a customer
        5 - Exit
    """
    print(menu)
    selection = int(input("please select a transaction : \n"))
    return selection

def Product():
    menu = """
        1 - List Product
        2 - Add new Product
        3 - Update Product
        4 - Delete a Product
        5 - Exit
    """
    print(menu)
    selection = int(input("please select a transaction : \n"))
    return selection