from user_profile import load_user_profile, save_user_profile

def main():
    print("🎮 Welcome to Quiz Builder Game!")
    username = input("Enter your name: ")
    profile = load_user_profile(username)

    print(f"\nWelcome, {profile['name']}!")
    print(f"❤️ Hearts: {profile['hearts']}")
    print(f"💰 Coins: {profile['coins']}")
    print(f"🏡 Your House: {', '.join(profile['house']) if profile['house'] else 'Nothing yet'}")

if __name__ == "__main__":
    main()
