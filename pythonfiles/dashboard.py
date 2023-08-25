import json


def add_room(room_name):
    # Load existing data from the JSON file
    try:
        with open('rooms.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Add the new room to the data with count 0 and an empty model list
    data[room_name] = {"count": 0, "model": []}

    # Write the updated data back to the JSON file
    with open('rooms.json', 'w') as file:
        json.dump(data, file, indent=4)


def add_model_to_room(model_name, room_name):
    new_model = {}
    new_model["Model"] = str(model_name)
    new_model["Status"] = "Ok"
    new_model["Problem"] = "Nil"

    # Load existing data from the JSON file
    try:
        with open('rooms.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Check if the room exists in the data
    if room_name in data:
        # Add the model to the room's model list
        data[room_name]["model"].append(new_model)
        # Increment the room's count
        data[room_name]["count"] += 1
    else:
        print(f"Room '{room_name}' does not exist.")

    # Write the updated data back to the JSON file
    with open('rooms.json', 'w') as file:
        json.dump(data, file, indent=4)


def makeProblem(roomnumber, model):
    try:
        with open('rooms.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Check if the room exists in the data
    if roomnumber in data:
        # Add the model to the room's model list
        for i in data[roomnumber]["model"]:
            if i["Model"] == model:
                i["Status"] = "No"
                print("yes")
        # Increment the room's count
    else:
        print(f"Room '{roomnumber}' does not exist.")

    # Write the updated data back to the JSON file
    with open('rooms.json', 'w') as file:
        json.dump(data, file, indent=4)