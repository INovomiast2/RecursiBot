import datetime
from utils.colors import *

# Get the current day
date = datetime.datetime.now()

# Format the current day
formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")

# Prints the date
print(bold + black + formatted_date + blue, "INFO", reset + magenta, "   system.files", reset, "colors imported correctly")