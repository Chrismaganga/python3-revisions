from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")
print("Current Time:", current_time)

# sec
import random

def random_time():
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

print("Random Time:", random_time())

# third
from datetime import timedelta

def generate_time_intervals(start="00:00:00", interval_minutes=30, count=5):
    start_time = datetime.strptime(start, "%H:%M:%S")
    return [(start_time + timedelta(minutes=i * interval_minutes)).strftime("%H:%M:%S") for i in range(count)]

print(generate_time_intervals(start="08:00:00", interval_minutes=15, count=4))
