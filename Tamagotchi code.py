# %%
import time
import random 

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 0
        self.energy = 100
        self.is_alive = True
        self.partner = None
        self.kids = 0

    def feed(self):
        if self.is_alive:
            print(f"{self.name} is being fed.")
            self.hunger -= 10
            self.energy += 5
            self.happiness += 3
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't feed it.")

    def play(self):
        if self.is_alive:
            print(f"{self.name} is playing.")
            self.hunger += 5
            self.energy -= 10
            self.happiness += 7
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't play with it.")

    def play_at_playground(self):
        if self.is_alive:
            print(f"{self.name} is playing at the playground.")
            self.hunger += 3
            self.energy -= 5
            self.happiness += 10
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't play with it.")

    def play_soccer(self):
        if self.is_alive:
            print(f"{self.name} is playing soccer.")
            self.hunger += 5
            self.energy -= 15
            self.happiness += 12
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't play with it.")
    
    def go_to_school(self):
        if self.is_alive:
            print(f"{self.name} is going to school.")
            self.hunger += 5
            self.energy -= 10
            self.happiness += 8
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. It can't go to school.")
            
    def go_to_cafe(self):
        if self.is_alive:
            print(f"{self.name} is going to the cafe.")
            self.hunger -= 8
            self.energy += 10
            self.happiness += 15
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't go to the cafe with it.")

    def have_beer(self):
        if self.is_alive:
            print(f"{self.name} is having beer.")

            # Adjust hunger, energy, and happiness based on having beer
            self.hunger -= 8
            self.energy -= 5
            self.happiness += 15

            self._update_status()
        else:
            print(f"{self.name} is no longer alive. It can't have beer.")
            
    def go_to_shopping(self):
        if self.is_alive:
            print(f"{self.name} is going shopping.")
            self.hunger += 3
            self.energy -= 5
            self.happiness += 10
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't go shopping with it.")
    
    def watch_netflix_at_night(self):
        if self.is_alive:
            print(f"{self.name} is watching Netflix at night.")
            self.energy -= 10
            self.happiness += 15
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. It can't watch Netflix.")
        
    def go_on_date(self):
            if self.is_alive:
                print(f"{self.name} is going on a date with their partner.")

                # Randomly choose a date activity
                date_activity = random.choice(["movie", "restaurant", "park"])
                
                # Adjust hunger, energy, and happiness based on the chosen activity
                if date_activity == "movie":
                    self.hunger += 5
                    self.energy -= 15
                    self.happiness += 25
                elif date_activity == "restaurant":
                    self.hunger -= 10
                    self.energy -= 10
                    self.happiness += 30
                elif date_activity == "park":
                    self.hunger += 3
                    self.energy -= 5
                    self.happiness += 20

                # Add a chance for a surprise event during the date
                if random.random() < 0.2:  # 20% chance for a surprise event
                    print("Surprise event! Your date found a hidden treasure.")
                    self.happiness += 50

                self._update_status()
            else:
                print(f"{self.name} is no longer alive. You can't go on a date with it.")
    
    def talk_to_friends(self):
        if self.is_alive:
            print(f"{self.name} is talking to friends.")
            self.happiness += 10
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. It can't talk to friends.")
    
    def walk_with_dogs(self):
        if self.is_alive:
            print(f"{self.name} is walking with dogs.")
            self.happiness += 20
            self.energy -= 10
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. It can't walk with dogs.")

    def sleep(self):
        if self.is_alive:
            print(f"{self.name} is going to sleep.")
            self.hunger += 5
            self.energy += 15
            self.happiness += 5
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't make it sleep.")

    def get_married(self, partner_name):
        if self.is_alive:
            print(f"{self.name} is getting married to {partner_name}.")
            self.partner = partner_name
            self.happiness += 30
            self._update_status()
        else:
            print(f"{self.name} is no longer alive. You can't get it married.")

    def raise_kids(self, num_kids):
        if self.is_alive and self.partner is not None:
            print(f"{self.name} and {self.partner} are raising {num_kids} kids.")
            self.kids += num_kids
            self.happiness += 10 * num_kids
            self._update_status()
        else:
            print(f"{self.name} or {self.partner} is no longer alive, or you are not married. You can't raise kids.")

    def _update_status(self):
        self.hunger = max(0, min(self.hunger, 100))
        self.energy = max(0, min(self.energy, 100))
        self.happiness = max(0, min(self.happiness, 100))

        if self.hunger >= 100 or self.energy <= 0 or self.happiness <= 0:
            self.is_alive = False
            print(f"{self.name} has passed away. Game over.")

    def check_status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Partner: {self.partner}")
        print(f"Number of Kids: {self.kids}")
        print("Is alive: Yes" if self.is_alive else "Is alive: No")

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
# %%
