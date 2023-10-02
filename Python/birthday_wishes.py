import datetime

# Dictionary of friends' and family members' birthdays
birthdays = {
    "Friend1": "1990-03-15",
    "Friend2": "1985-07-20",
    # Add more entries here
}

# Function to send birthday wishes
def send_birthday_wishes(name):
    message = f"Happy Birthday, {name}! 🎂🎉"
    # Send the message (e.g., via email or messaging platform)

# Get the current date
today = datetime.date.today()

# Check for birthdays
for name, birthday in birthdays.items():
    b_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    if b_date.month == today.month and b_date.day == today.day:
        send_birthday_wishes(name)
