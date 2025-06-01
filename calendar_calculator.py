# Currently have input of time, verification of integer entry, conversion to list, conversion to days.
# Need subtraction of start/end days, then conversion to years/months/weeks/days.

import math
import os


month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


month_names = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}


day_names = {
    "Saturday": 0,
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6
}


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Calendar Calculator!\n")
    date = date_select()
    total_days = total_days_calculator(date)
    date_name(date, total_days)
        
        
def date_name(date, total_days):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{weekday_calculator(total_days)}, the {day_calculator(date)} of {month_calculator(date)}, {date[2]}")


def date_select():
    print("Please enter a date using the following format:")
    while True:
        date = input(
        "dd/mm/yyyy\n"
        "\n"
        )
        os.system('cls' if os.name == 'nt' else 'clear')
        date = date.split("/")
        if verify_format(date) == True:
            return(date)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(
                "Please re-enter your date using only numbers and following the displayed format below:"
                )


def verify_format(date):
    if list(map(len, date)) == [2, 2, 4]:
        for item in date:
            if item.isalpha() == False:
                return True


def total_days_calculator(date):
    date = list(map(int, date))
    years = (date[2] * 365) + math.floor(date[2] / 4)
    days = date[0]
    for key, value in month_days.items():
        if int(key) >= 1 and int(key) <= (date[1] + 1):
            days += value
    return years + days


def weekday_calculator(total_days):
    weekday = (total_days % 7) + 1
    for key, value in day_names.items():
        if weekday == value:
            return key


def day_calculator(date):
    if date[0] == "01":
        return "1st"
    elif date[0] == "02":
        return "2nd"
    elif date[0] == "03":
        return "3rd"
    else:
        return str(date[0]) + "th"


def month_calculator(date):
    for key, value in month_names.items():
        if date[1] == value:
            return key


main()

