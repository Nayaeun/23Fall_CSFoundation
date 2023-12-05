# %%
import time

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
# %%
