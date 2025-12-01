class Pokemon:
    def __init__(self, name, type_, level):
        self.name = name
        self.type = type_
        self.level = level

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Level: {self.level})"

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to {self.level}!")

    def attack(self, move):
        print(f"{self.name} used {move}!")