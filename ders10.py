import ders10screen,ders10menu

ders10screen.clear()

mesaj = """
    data management system

    choose one of the following actions

"""
print(mesaj)

transactions = ["Customer","Product","Stock","Sales"]

selection = ders10menu.customer()

print(f" You have {selection} operation numbered.")

input()