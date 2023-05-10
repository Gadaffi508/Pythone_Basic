enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
#print(potion_strength) //dışardan erişilmez

player_health = 10

def game():
    def drink_potions():
        potion_strength = 2
        print(player_health)
    drink_potions()

print(player_health)

game_level = 3

def create_enemy():
    enemies = ["skeleton","Zombie","Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()