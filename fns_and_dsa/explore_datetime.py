from datetime import timedelta, date, datetime

def display_current_datetime():
    current_date = datetime.now()
    print('Current date and time:',current_date)


def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = date.today() + timedelta(days=number_of_days)
    print('Future date: ',future_date)
    return future_date


display_current_datetime()
calculate_future_date()