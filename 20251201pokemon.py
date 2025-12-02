import random
import time

class Pokemon:
    def __init__(self, name, type_, level):
        self.name = name
        self.type = type_
        self.level = level

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Level: {self.level})"

    def level_up(self):
        self.level += 1
        print(f"{self.name} はレベル {self.level} にあがった!")

    def attack(self, move):
        print(f"{self.name} は {move} をつかった!")

class heldpokemon( Pokemon ):
    def __init__(self, name, type_, level, held_item):
        super().__init__(name, type_, level)
        self.held_item = held_item

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Level: {self.level}, Held Item: {self.held_item})"

def catch_pokemon(pokemon):
    catch_rate = random.randint(1, 100) + (pokemon.level/2)

    if catch_rate < 50:
        print(f"やったー！{pokemon.name}をつかまえたぞ!")
        return True
    else:
        print(f"{pokemon.name}はにげだした!")
        return False
    
def main():
    pokemons = [
        Pokemon("ププンププ", "ゴースト", 5),
        Pokemon("ヤミカラス", "あく", 25),
        Pokemon("イトマル", "むし", 70),
        Pokemon("ヤブクロン", "どく", 2)
    ]
    while True:
        selected_pokemon = random.choice(pokemons)
        print(f"やせいの{selected_pokemon.name} があらわれた!")
        time.sleep(2)
        print("モンスターボールを投げた!")
        time.sleep(2)
        caught = catch_pokemon(selected_pokemon)
        if caught:
            break
        else:
            print("もういちどやる？?y/n")
            if input().lower() =='y':
                continue
            else:
                return

    time.sleep(2)
    print(f"ポケモンのステータス: {selected_pokemon}")
    print(f"つかまえた {selected_pokemon}にニックネームをつけますか?y/n")
    if input().lower() == 'y':
        print("ニックネームを入力してください:")
        nickname = input()
        print(f"{selected_pokemon.name}のニックネームは{nickname}になりました!")
        selected_pokemon.name = nickname
    else:
        print("ニックネームはつけませんでした。")


if __name__ == "__main__":
    main()
    
#ランダムに１匹選択
#捕獲メソッドの実行
#パラメータの表示