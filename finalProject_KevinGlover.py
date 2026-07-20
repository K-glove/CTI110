#Kevin Glover
#2026-09-19
#Final Project
#Legendary Battle Simulator

import random

created_characters = []


def allocate_stats():
    """Allocate exactly 100 points, with at least one point in each stat."""
    stats = {}
    stat_names = ["health", "attack", "defense", "magic"]
    points_left = 100

    print("\nYou have 100 stat points to spend.")
    print("Each stat must receive at least 1 point.")

    for position, stat_name in enumerate(stat_names):
        remaining_stats = len(stat_names) - position - 1
        maximum = points_left - remaining_stats

        while True:
            choice = input(
                f"Assign points to {stat_name.title()} "
                f"(1-{maximum}; {points_left} remaining): "
            ).strip()
            if choice.isdigit() and 1 <= int(choice) <= maximum:
                stats[stat_name] = int(choice)
                points_left -= int(choice)
                break
            print(f"Enter a whole number from 1 to {maximum}.")

    return stats


def create_character():
    """Create and save one playable character."""
    print("\n--- Create Character ---")
    name = input("Enter your character's name: ").strip()
    if not name:
        name = f"Hero {len(created_characters) + 1}"

    character = allocate_stats()
    character["name"] = name
    character["max_health"] = character["health"]
    created_characters.append(character)

    print(f"\n{name} was created!")


def view_characters():
    """Display every character that has been created."""
    print("\n--- Created Characters ---")
    if not created_characters:
        print("No characters have been created yet.")
        return

    for number, character in enumerate(created_characters, start=1):
        print(
            f"{number}. {character['name']} | "
            f"Health: {character['max_health']} | Power: {character['attack']} | "
            f"Defense: {character['defense']} | Magic: {character['magic']}"
        )


def choose_fighter(prompt, unavailable_index=None):
    """Choose one saved character, optionally excluding the first fighter."""
    while True:
        choice = input(prompt).strip()
        if not choice.isdigit():
            print("Please enter a character number.")
            continue

        index = int(choice) - 1
        if index < 0 or index >= len(created_characters):
            print("That character does not exist.")
        elif index == unavailable_index:
            print("Choose a different character.")
        else:
            return index


def calculate_damage(attacker, defender):
    """Return a randomized damage amount based on both fighters' stats."""
    attack_roll = random.randint(attacker["attack"] // 2, attacker["attack"])
    defense_roll = random.randint(defender["defense"] // 3, defender["defense"])
    magic_bonus = random.randint(0, attacker["magic"] // 4)
    return max(1, attack_roll + magic_bonus - defense_roll)


def start_game():
    """Run a battle between two selected characters."""
    if len(created_characters) < 2:
        print("\nCreate at least two characters before starting a game.")
        return

    view_characters()
    print("\n--- Choose Fighters ---")
    first_index = choose_fighter("Choose fighter 1: ")
    second_index = choose_fighter("Choose fighter 2: ", first_index)

    fighter_one = created_characters[first_index].copy()
    fighter_two = created_characters[second_index].copy()
    fighter_one["health"] = fighter_one["max_health"]
    fighter_two["health"] = fighter_two["max_health"]

    fighters = [fighter_one, fighter_two]
    turn = random.randint(0, 1)
    print(f"\n--- {fighter_one['name']} vs. {fighter_two['name']} ---")

    round_number = 1
    while fighter_one["health"] > 0 and fighter_two["health"] > 0:
        attacker = fighters[turn]
        defender = fighters[1 - turn]
        damage = calculate_damage(attacker, defender)
        defender["health"] = max(0, defender["health"] - damage)

        print(
            f"Round {round_number}: {attacker['name']} attacks {defender['name']} "
            f"for {damage} damage. {defender['name']} has {defender['health']} health left."
        )
        if defender["health"] == 0:
            print(f"\n{attacker['name']} wins the battle!")
            break

        turn = 1 - turn
        round_number += 1


def main_menu():
    """Show the game menu until the user chooses to quit."""
    while True:
        print("\n=== Legendary Battle Simulator ===")
        print("1. View created characters")
        print("2. Create a new character")
        print("3. Start a new game")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            view_characters()
        elif choice == "2":
            create_character()
        elif choice == "3":
            start_game()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main_menu()


