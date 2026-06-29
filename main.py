print("Emergent Misalignment MAS Simulator")
print("Version 1: baby command-line simulation")

rooms = [
    {
        "name": "Room A",
        "is_available": True,
        "is_comfortable": True,
    },
    {
        "name": "Room B",
        "is_available": True,
        "is_comfortable": False,
    }
]


print(rooms)
print(f"First room name: {rooms[0]['name']}")
print(f"Second room name: {rooms[1]['name']}")


print("\nChecking rooms:")
for room in rooms:
    if room["is_available"] and room["is_comfortable"]:
        print(f"{room['name']} is suitable for welfare session.")
    else:
        print(f"{room['name']} is not suitable for welfare session.")

booked_room = None

for room in rooms:
    if room["is_available"] and room["is_comfortable"]:
        booked_room = room
        room["is_available"] = False  # Mark the room as booked
        print(f"\nStudent Services Bot booked {room['name']} for welfare session.")
        break

print(f"Booked room: {booked_room['name']}")

print("\nEnergy Manager checks the booked room:")
booked_room["is_comfortable"] = False
print(f"Energy Manager reduced heating and lighting in {booked_room['name']}.")
print(f"{booked_room['name']} is now unsuitable for the welfare session.")
