# Modifying Global Scope

enemies = 1


#def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


def increase_enemies(enemy):
    print(f"enemies outside function: {enemies}")
    return enemy +1

enemies = increases_enemies(enemies)

print(f"enemies inside function: {enemies}")

