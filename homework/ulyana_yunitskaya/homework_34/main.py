from datetime import datetime


days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

today = datetime.now()

day_name = days[today.weekday()]

print('=== My Docker Python Program ===')
print(f'Today is {day_name}')
print(f"Date: {today.strftime('%d.%m.%Y')}")

if today.weekday() < 5:
    print('It is a working day. Have a productive day!')
else:
    print('It is a weekend. Time to relax and enjoy your day!')
