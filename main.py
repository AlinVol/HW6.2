def convert_seconds(seconds):
    if not (0 <= seconds < 8640000):
        return "Input should be between 0 and 8640000."

    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    formatted_time = f"{days} day{'s' if days != 1 else ''}, " \
                     f"{str(hours).zfill(2)}:" \
                     f"{str(minutes).zfill(2)}:" \
                     f"{str(seconds).zfill(2)}"

    return formatted_time

user_input = int(input("Enter the number of seconds (0 to 8640000): "))
print(convert_seconds(user_input))
