def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934

def get_miles():
    """Prompt the user to enter miles and validate the input."""
    while True:
        try:
            miles = float(input("Enter miles: ").strip())
        except ValueError:
            print("Invalid input.")
            continue
        if miles < 0:
            print("Cannot be negative.")
            continue
        return miles

def main():
    """Main function to run the miles to kilometers converter."""
    print("=" * 30)
    print("Welcome In Miles to Kilometers Converter")
    print("=" * 30)
    while True:
        print("\n1. Convert\n2. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            miles = get_miles()
            print(f"{miles} miles = {miles_to_km(miles):.4f} km")
        elif choice == "2":
            print("Goodbye! See you next time! ")
            break
        else:
            print("Please enter 1 or 2.")

if __name__ == "__main__":
    main()