import time

# Define reminders
reminders = [
    "Reminder 1: Call Mom at 3:00 PM.",
    "Reminder 2: Buy groceries on your way home.",
    # Add more reminders here
]

# Function to display reminders
def display_reminders():
    for reminder in reminders:
        print(reminder)

# Schedule reminders for a specific time (e.g., 3:00 PM)
while True:
    current_time = time.localtime()
    if current_time.tm_hour == 15 and current_time.tm_min == 0:
        display_reminders()
    time.sleep(60)  # Check the time every minute
