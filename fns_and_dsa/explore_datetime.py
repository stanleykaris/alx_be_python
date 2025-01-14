import datetime
from datetime import timedelta

def display_current_datetime():
    current_datetime = datetime.datetime.now()
    print(f"Current Date and Time: {current_datetime.strftime("%Y-%m-%d %H:%M:%S")}")
    return current_datetime

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add: "))
    current_date = datetime.date.today()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date after {number_of_days} days: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return future_date

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
    