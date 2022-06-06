# unit = "hours"
calc_to_unit = 24


def days_to_units(days, unit):
    if unit == "hours":
        print(f"{days} days is equivalent to {days * 24} {unit}")
    elif unit == "minutes":
        print(f"{days} days is equivalent to {days * 24 * 60} {unit}")
    else:
        return "unit not valid "


def validate_and_execute():
    try:
        user_input = int(days_and_units_dictionary["days"])

        # do conversion for positive numbers only
        if user_input > 0:
            return days_to_units(user_input, days_and_units_dictionary["unit"])
        elif user_input == 0 or user_input > 0:
            print("Enter more than zero")
        else:
            print("number is negative be positive in your life man")
    except ValueError:
        print("Input is not a number, enter a number!")


num_of_days = ""
while num_of_days != "except":
    num_of_days = input("Enter the number days to convert\n")
    list_of_days = num_of_days.split(":")
    days_and_units_dictionary = {"days": list_of_days[0], "unit": list_of_days[1]}
    validate_and_execute()
