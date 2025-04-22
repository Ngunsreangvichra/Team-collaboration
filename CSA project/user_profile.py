import os

# Load or create user profile
def load_user_profile(username):
    filename = f"{username}.txt"
    profile = {
        "name": username,
        "hearts": 0,
        "coins": 0,
        "house": []
    }

    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                key, value = line.strip().split(":")
                if key == "house":
                    profile["house"] = value.split(",") if value else []
                else:
                    profile[key] = int(value) if value.isdigit() else value
    else:
        save_user_profile(profile)  # create file if not exists

    return profile

# Save profile to file
def save_user_profile(profile):
    filename = f"{profile['name']}.txt"
    with open(filename, "w") as file:
        file.write(f"name:{profile['name']}\n")
        file.write(f"hearts:{profile['hearts']}\n")
        file.write(f"coins:{profile['coins']}\n")
        file.write(f"house:{','.join(profile['house'])}\n")

