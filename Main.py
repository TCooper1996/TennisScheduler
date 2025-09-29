
# 📝 Table sign-up sheet

# List to store all players (each player is a dictionary with name, age, and slot)
players = []

# Dictionary of available time slots
# Each slot has its own list of players
time_slots = {
    "10:00 AM": [],
    "11:00 AM": [],
    "12:00 PM": [],
}

# Limits
MAX_PER_SLOT = 1   # maximum players per time slot
MAX_PLAYERS = 3    # maximum players overall
MIN_AGE = 6        # minimum age allowed
MAX_AGE = 65       # maximum age allowed

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
    for slot, signed_up in time_slots.items():
        print(f"- {slot} ({len(signed_up)}/{MAX_PER_SLOT} spots taken)")

    # Ask the user to choose a slot
    chosen_slot = input("Enter your preferred time slot: ")

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
