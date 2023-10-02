# Initialize daily step count
daily_steps = 0

# Function to record steps
def record_steps(steps):
    global daily_steps
    daily_steps += steps

# Function to display daily steps
def display_daily_steps():
    print(f"Today's Steps: {daily_steps}")

# Record steps throughout the day (e.g., during workouts)
record_steps(2500)
record_steps(3000)

# Display the daily step count
display_daily_steps()
