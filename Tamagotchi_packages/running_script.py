# running script
import time
import random
from tamagotchi.Tamagotchi import Tamagotchi

if __name__ == "__main__":
    pet_name = input("Enter your Tamagotchi's name: ")
    tamagotchi = Tamagotchi(pet_name)

    while tamagotchi.is_alive:
        action = input("What do you want to do? (feed/play/play_at_playground/play_soccer/go_to_school/go_on_date/sleep/get_married/raise_kids/quit): ").lower()

        if action == "feed":
            tamagotchi.feed()
        elif action == "play":
            tamagotchi.play()
        elif action == "play_at_playground":
            tamagotchi.play_at_playground()
        elif action == "play_soccer":
            tamagotchi.play_soccer()
        elif action == "go_to_school":
            tamagotchi.go_to_school()
        elif action == "go_on_date":
            tamagotchi.go_on_date()
        elif action == "sleep":
            tamagotchi.sleep()
        elif action == "get_married":
            partner_name = input("Enter the name of your partner: ")
            tamagotchi.get_married(partner_name)
        elif action == "raise_kids":
            num_kids = int(input("Enter the number of kids to raise: "))
            tamagotchi.raise_kids(num_kids)
        elif action == "quit":
            print("Quitting the game.")
            break
        else:
            print("Invalid action. Please enter 'feed', 'play', 'play_at_playground', 'play_soccer', 'go_on_date', 'sleep', 'get_married', 'raise_kids', or 'quit'.")

        time.sleep(1)  # simulate the passage of time

        tamagotchi.check_status()