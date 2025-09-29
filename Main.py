
# 📝 Table sign-up sheet

# Limits
import json


MAX_PER_SLOT = 1   # maximum players per time slot
MAX_PLAYERS = 3    # maximum players overall
MIN_AGE = 6        # minimum age allowed
MAX_AGE = 65       # maximum age allowed


class TIME_SLOTS:
    def __init__(self, time, attendee, max_slots):
        self.time = time
        self.attendee = attendee
        self.max_slots = max_slots
        
# List to store all players (each player is a dictionary with name, age, and slot)
players = []

# Dictionary of available time slots
# Each slot has its own list of players\
time_slots = [
    TIME_SLOTS('10:00 AM', [], MAX_PER_SLOT),
    TIME_SLOTS('11:00 AM', [], MAX_PER_SLOT),
    TIME_SLOTS('12:00 PM', [], MAX_PER_SLOT)
]


# Keep asking for players until we reach the maximum
while len(players) < MAX_PLAYERS:
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))

    # Check age restriction
    if age < MIN_AGE or age > MAX_AGE:
        print('❌ Sorry, must be between the age 6 thru 65.')
        continue

    # Show available time slots
    print("\nAvailable time slots: ")
    for i, t in enumerate(time_slots):
        print(f"{i} - {t.time} ({len(t.attendee)}/{t.max_slots} spots taken)")
      
    # Ask the user to choose a slot
    chosen_slot_index = input("Enter your preferred time slot: ")
    chosen_slot = time_slots[int(chosen_slot_index)]
    print(json.dumps(chosen_slot))

    # Check if the slot exists
    if chosen_slot not in time_slots:
        print("❌ Invalid slot. Please choose a valid time slot.")
        continue

    # Check if the slot is already full
    if len(time_slots[chosen_slot]) >= MAX_PER_SLOT:
        print("❌ That time slot is full. Please choose another one.")
        continue

    # Create a dictionary for this player
    player_info = {'name': name, 'age': age, 'slot': chosen_slot}

    # Add to global player list
    players.append(player_info)

    # Add to the chosen slot list
    time_slots[chosen_slot].append(player_info)

    # Confirm sign-up
    print(f'✅ {name} has been added to {chosen_slot}! '
          f'({len(players)}/{MAX_PLAYERS} total players)')


# Once max players reached, show the final list
print('\n🎉 Sign-up is full! Here is the list of players:')
for player in players:
    print(f"- {player['name']} (age {player['age']}) - Slot: {player['slot']}")
