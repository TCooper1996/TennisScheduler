
# 📝 Table sign-up sheet

import json
from typing import List


# Limits
MAX_PER_SLOT = 1   # maximum players per time slot
MAX_PLAYERS = 3    # maximum players overall
MIN_AGE = 6        # minimum age allowed
MAX_AGE = 65       # maximum age allowed

# Bundles all data that represents a single Attendee
# eg: a = Attendee("Denny", 69)
class Attendee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_string(self):
        return f"Name: {self.name}, Age: {self.age}"

# Bundles all data that represents a timeslot
# eg: t = Timeslot("12:35 AM", [Attendee("Denny", 69)], 3)
class Timeslot:
    # Note the text after each colon; those are type annotations, which simply indicate what "type" of data each variable is expected to have
    # Type annotations have absolutely zero effect on the behavior of the app and are completely optional, though recommended for readability
    def __init__(self, time: str, attendees: List[Attendee], max_slots: int):
        self.time = time
        self.attendees = attendees
        self.max_slots = max_slots

    # Creates a string representation of a timeslot which can be printed
    def to_string(self):
        # We use the to_string method defined in the Attendee class to convert each attendee into a string and add all the strings to one big string
        attendees_string = ""
        for attendee in self.attendees:
            attendees_string = attendees_string + "\n" + attendee.to_string()

        return f"Time: {self.time}\nMax Slots: {self.max_slots}, Attendees: {attendees_string}"        

# -----------------------------


# Our main function, this is the "high level" outline of our app, where the app begins and ends
def main():
    # Each slot has its own list of players
    time_slots = [
        Timeslot('10:00 AM', [], MAX_PER_SLOT),
        Timeslot('11:00 AM', [], MAX_PER_SLOT),
        Timeslot('12:00 PM', [], MAX_PER_SLOT)
    ]

    # Keep asking for players until we reach the maximum
    while len(get_all_players(time_slots)) < MAX_PLAYERS:
        # Take the users info and create an attendee
        attendee = enter_personal_info()

        # Choose a time slot
        time_slot = choose_time_slot(time_slots)
        
        # Add attendee to this time_slot
        time_slot.attendees.append(attendee)

        # Confirm sign-up
        print(f'✅ {attendee.name} has been added to {time_slot.time}! '
            f'({len(time_slot.attendees)}/{time_slot.max_slots} total players)')


    # Once max players reached, show the final list
    print('\n🎉 Sign-up is full! Here is the list of players:')
    for player in get_all_players(time_slots):
        print(f"- Name: {player.name}, Age: {player.age}")

#----------------------


# Helper functions that main uses 

# returns a list of all Attendees in the given time_slots
def get_all_players(time_slots) -> List[Attendee]:
    # Since each timeslot holds its own players, use this function to view all players across all slots
    players = []
    for t in time_slots:
        # Use .extend to add a list of items to an existing list, use .append to add a single item
        players.extend(t.attendees)
    return players

def enter_personal_info() -> Attendee:
    # Infinite loop until the return is reached
    while True:
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))

        # Check age restriction
        if age < MIN_AGE or age > MAX_AGE:
            print('❌ Sorry, must be between the age 6 thru 65.')
            continue

        # If all rules pass, return the Attendee object
        return Attendee(name, age)

def choose_time_slot(time_slots) -> Timeslot:
    # We put the time slot selection into its own loop so that if the user chooses an incorrect timeslot, they dont have to re-enter their name and age
    while True:
        print("\nAvailable time slots: ")
        for i, t in enumerate(time_slots):
            print(f"{i} - {t.time} ({len(t.attendees)}/{t.max_slots} spots taken)")
        
        # Ask the user to choose a slot
        chosen_slot_index = int(input(f"Enter your preferred time slot: (0-{len(time_slots)-1})"))

        # Selected index must be between 0 and len(attendees)
        if chosen_slot_index < 0 or chosen_slot_index >= len(time_slots):
            print("❌ Invalid slot. Please choose a valid time slot.")
            # Reset from beginning of loop
            continue

        chosen_slot = time_slots[chosen_slot_index]
        # Check if the slot is already full
        if len(chosen_slot.attendees) >= MAX_PER_SLOT:
            print("❌ That time slot is full. Please choose another one.")
            # Reset from beginning of loop
            continue

        # Return the chosen timeslot
        return chosen_slot

if __name__ == "__main__":
    main()