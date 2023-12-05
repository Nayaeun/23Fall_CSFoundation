# running script
import time
import random
from tamagotchi.Tamagotchi import Tamagotchi

# Example usage
if __name__ == "__main__":
    pet_name = input("Enter your Tamagotchi's name: ")
    tamagotchi = Tamagotchi(pet_name)

    while tamagotchi.is_alive:
        print("Select the number for action:")
        print("1. Feed\n2. Play\n3. Play at Playground\n4. Play Soccer\n5. Go to School\n6. Go to Cafe\n7. Have Beer\n8. Watch Netflix at Night\n9. Go Shopping\n10. Go on a Date\n11. Talk to Friends\n12. Walk with Dogs\n13. Sleep\n14. Get Married\n15. Raise Kids\n16. Quit")

        try:
            action = int(input("Enter the number corresponding to the action: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if action == 1:
            tamagotchi.feed()
        elif action == 2:
            tamagotchi.play()
        elif action == 3:
            tamagotchi.play_at_playground()
        elif action == 4:
            tamagotchi.play_soccer()
        elif action == 5:
            tamagotchi.go_to_school()
        elif action == 6:
            tamagotchi.go_to_cafe()
        elif action == 7:
            tamagotchi.have_beer()
        elif action == 8:
            tamagotchi.watch_netflix_at_night()
        elif action == 9:
            tamagotchi.go_to_shopping()
        elif action == 10:
            tamagotchi.go_on_date()
        elif action == 11:
            tamagotchi.talk_to_friends()
        elif action == 12:
            tamagotchi.walk_with_dogs()
        elif action == 13:
            tamagotchi.sleep()
        elif action == 14:
            partner_name = input("Enter the name of your partner: ")
            tamagotchi.get_married(partner_name)
        elif action == 15:
            num_kids = int(input("Enter the number of kids to raise: "))
            tamagotchi.raise_kids(num_kids)
        elif action == 16:
            print("Quitting the game.")
            break
        else:
            print("Invalid action. Please enter a number between 1 and 16.")

        time.sleep(1)  # simulate the passage of time

        tamagotchi.check_status()