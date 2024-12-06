from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def prepare_user_list(user_data):
    res=[]
    for user in user_data:
       res.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    
    return res

def find_next_weekday(start_date, weekday):
 
    start_weekday = start_date.weekday()
    if  start_weekday >= weekday :
        weekday += 7
    
    return start_date + timedelta(days = weekday - start_weekday)
    
         
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]

start_d = string_to_date("2024.12.06")
print(find_next_weekday(start_d, 4)) 

#print(prepare_user_list(users))
#[ {"name": user["name"], "birthday": string_to_date(user["birthday"])} for user in users ]