class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"Part: {self.name}, Material: {self.material}"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}

    def add_part(self, part):
        self.__parts[part.name] = part

    def display_state(self):
        state = f"State of the ship {self.name}:\n"
        for part in self.__parts.values():
            state += f"{part}\n"
        return state

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
        else:
            print(f"Part {part_name} not found.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
        else:
            print(f"Part {part_name} not found.")

class ShipMenu:
    def __init__(self, ship):
        self.ship = ship
        self.history = []

    def display_menu(self):
        print("\nMenu:")
        print("1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Quitter")

    def replace_part(self):
        part_name = input("Entrez le nom de la pièce à remplacer: ")
        new_name = input("Entrez le nom de la nouvelle pièce: ")
        new_material = input("Entrez le matériau de la nouvelle pièce: ")
        new_part = Part(new_name, new_material)
        self.ship.replace_part(part_name, new_part)
        self.history.append(f"Remplacé {part_name} par {new_name} en {new_material}.")

    def change_material(self):
        part_name = input("Entrez le nom de la pièce à modifier: ")
        new_material = input("Entrez le nouveau matériau: ")
        self.ship.change_part(part_name, new_material)
        self.history.append(f"Modifié le matériau de {part_name} en {new_material}.")

    def display_history(self):
        print("Historique des modifications:")
        for entry in self.history:
            print(entry)

# Exemple d'utilisation
boat = Ship("Bateau1")
mast = Part("Mât", "Bois")
boat.add_part(mast)
menu = ShipMenu(boat)

# Affichage initial de l'état
print(boat.display_state())  # Utilisation de print() pour afficher l'état

while True:
    menu.display_menu()
    choice = input("Choisissez une option: ")

    if choice == '1':
        print(boat.display_state())  # Affichage de l'état
    elif choice == '2':
        menu.replace_part()
    elif choice == '3':
        menu.change_material()
    elif choice == '4':
        menu.display_history()
    elif choice == '5':
        break
    else:
        print("Option invalide.")