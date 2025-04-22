def convert_hearts_to_coins(profile):
    print("\n💱 Convert Hearts to Coins")
    print(f"You have ❤️ {profile['hearts']} hearts.")
    if profile["hearts"] < 10:
        print("You need at least 10 hearts to convert.")
        return

    max_convert = profile["hearts"] // 10
    print(f"You can convert up to {max_convert} coins.")

    try:
        amount = int(input("How many coins do you want to convert to? "))
        if 0 < amount <= max_convert:
            hearts_spent = amount * 10
            profile["hearts"] -= hearts_spent
            profile["coins"] += amount
            print(f"✅ Converted {hearts_spent} hearts to {amount} coins!")
        else:
            print("❌ Invalid amount.")
    except ValueError:
        print("❌ Please enter a number.")
