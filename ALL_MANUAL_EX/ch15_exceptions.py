def get_number():
    while True:
        entry = input("Enter a number")
        try:
            entry = float(entry)
            return entry
        except ValueError:
            print("Not a number, try again")

print(get_number())