def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    day = 0
    if number == 1:
        day = 'Monday'
    elif number == 2:
        day = 'Tuesday'
    elif number == 3:
        day = 'Wednesday'
    elif number == 4:
        day = 'Thursaday'
    elif number == 5:
        day = 'Friday'
    elif number == 6:
        day = 'Saturday'
    elif number == 7:
        day = 'Sunday'
    else:
        return 'Iltimos 1dan 7gacha bolgan sonlarni kiriting'
    return day


print(main(1))
print(main(5))
print(main(7))
