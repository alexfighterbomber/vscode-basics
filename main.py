from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def find_next_weekday(start_date, weekday):
    start_weekday = start_date.weekday()
    if  start_weekday >= weekday : weekday += 7
    return start_date + timedelta(days = weekday - start_weekday)

def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5: birthday = find_next_weekday(birthday, 0)
    return birthday
           
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        birthday_this_year = user["birthday"].replace(year = today.year)
        if birthday_this_year < today:
            dateInNewYear = birthday_this_year.replace(year= today.year + 1)
            birthday_this_year = dateInNewYear
        is_fit = (birthday_this_year - today).days
        if 0 <= is_fit <= days:
            congratulation_date_str = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(congratulation_date_str)})
    return upcoming_birthdays

        
users = [
    {"name": "Bill Gates", "birthday": "1955.12.10"},
    {"name": "Steve Jobs", "birthday": "1955.12.11"},
    {"name": "Jinny Lee", "birthday": "1956.12.05"},
    {"name": "Sarah Lee", "birthday": "1957.08.26"},
    {"name": "Jonny Lee", "birthday": "1958.12.22"},
    {"name": "John Doe", "birthday": "1985.01.01"},
    {"name": "Jane Smith", "birthday": "1990.01.02"}
]

forPrint = get_upcoming_birthdays(prepare_user_list(users), 30)

print(forPrint)