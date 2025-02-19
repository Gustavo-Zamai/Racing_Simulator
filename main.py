import random
import asyncio

characters = [
    {'name':'Mario', 'speed': 4, 'handling': 3, 'power': 3, 'score': 0},
    {'name':'Luigi', 'speed': 3, 'handling': 4, 'power': 4, 'score': 0},
    {'name':'Donkey Kong', 'speed': 2, 'handling': 2, 'power': 5, 'score': 0},
    {'name':'Peach', 'speed': 3, 'handling': 4, 'power': 2, 'score': 0},
    {'name':'Bowser', 'speed': 5, 'handling': 2, 'power': 5, 'score': 0},
    {'name':'Toad', 'speed': 3, 'handling': 4, 'power': 3, 'score': 0},
    {'name':'Yoshi', 'speed': 2, 'handling': 4, 'power': 3, 'score': 0}
]

def pick_two_players():
    return random.randint(0, len(characters))

async def roll_dice():
    return random.randint(1, 6)


async def get_random_block():
    random_value = random.random()
    if random_value < 0.33:
        return "Straight"
    elif random_value < 0.66:
        return "Curve"
    else:
        return "Battle"


async def log_roll_result(character_name, block, dice_result, attribute):
    print(f"{character_name} 🎲 roll dice of {block} {dice_result} + {attribute} = {dice_result + attribute}")


async def play_race_engine(character1, character2):
    for round_num in range(1, 6):
        print(f"\n Round {round_num}")

        block = await get_random_block()
        print(f"Block: {block}")

        dice_result1 = await roll_dice()
        dice_result2 = await roll_dice()

        total_test_skill1, total_test_skill2 = 0, 0

        if block == "Straight":
            total_test_skill1 = dice_result1 + character1["speed"]
            total_test_skill2 = dice_result2 + character2["speed"]

            await log_roll_result(character1["name"], "speed", dice_result1, character1["speed"])
            await log_roll_result(character2["name"], "speed", dice_result2, character2["speed"])

        elif block == "Curve":
            total_test_skill1 = dice_result1 + character1["handling"]
            total_test_skill2 = dice_result2 + character2["handling"]

            await log_roll_result(character1["name"], "handling", dice_result1, character1["handling"])
            await log_roll_result(character2["name"], "handling", dice_result2, character2["handling"])

        elif block == "Battle":
            power_result1 = dice_result1 + character1["power"]
            power_result2 = dice_result2 + character2["power"]

            print(f"{character1['name']} battles with {character2['name']}! 🥊")

            await log_roll_result(character1["name"], "power", dice_result1, character1["power"])
            await log_roll_result(character2["name"], "power", dice_result2, character2["power"])

            if power_result1 > power_result2 and character2["score"] > 0:
                print(f"{character1['name']} wins the battle! {character2['name']} loss 1 point 🐢")
                character2["score"] -= 1
            elif power_result2 > power_result1 and character1["score"] > 0:
                print(f"{character2['name']} wins the battle! {character1['name']} loss 1 point 🐢")
                character1["score"] -= 1
            elif power_result1 == power_result2:
                print("It's a tie! No points lost")

        if total_test_skill1 > total_test_skill2:
            print(f"{character1['name']} score a point!")
            character1["score"] += 1
        elif total_test_skill2 > total_test_skill1:
            print(f"{character2['name']} score a point!")
            character2["score"] += 1

        print("-----------------------------")


async def declare_winner(character1, character2):
    print("Final Result:")
    print(f"{character1['name']}: {character1['score']} point(s)")
    print(f"{character2['name']}: {character2['score']} point(s)")

    if character1["score"] > character2["score"]:
        print(f"\n{character1['name']} wins the race! Congratulations! 🏆")
    elif character2["score"] > character1["score"]:
        print(f"\n{character2['name']} wins the race! Congratulations! 🏆")
    else:
        print("It's a tie!")


async def main():
    player1 = characters[pick_two_players()]
    player2 = characters[pick_two_players()]

    print(f"\n🚨 Race between {player1['name']} and {player2['name']} starting...\n")

    await play_race_engine(player1, player2)
    await declare_winner(player1, player2)


if __name__ == "__main__":
    asyncio.run(main())


