unit = "hours"
calc_to_unit = 24


def days_to_units(days):
    print(f"{days} days is equivalent to {days * calc_to_unit} {unit}")


def validate_and_execute():
    try:
        user_input = int(num_of_day)

        # do conversion for positive numbers only
        if user_input > 0:
            return days_to_units(user_input)
        elif user_input == 0 or user_input > 0:
            print("Enter more than zero")
        else:
            print("number is negative be positive in your life man")
    except ValueError:
        print("Input is not a number, enter a number!")


num_of_days = ""
while num_of_days != "except":
    num_of_days = input("Enter the number days to convert\n")
    print(type(num_of_days.split(",")))
    print(num_of_days.split(","))
    for num_of_day in num_of_days.split(","):
        validate_and_execute()
