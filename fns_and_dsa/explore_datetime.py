import datetime
from datetime import timedelta

def display_current_datetime():
    global current_date
    current_date = datetime.datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    


display_current_datetime()

def calculate_future_date():
    number_of_days = float(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print(future_date.strftime("%Y-%m-%d"))

calculate_future_date()