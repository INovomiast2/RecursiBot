import json

PATH_FILE = "config/config.json"

# Open json
def load_config():
	try:
		with open(PATH_FILE) as file:
			data = json.load(file)
			return data
	except FileNotFoundError:
		print("File not found")

# Save Prefix and Token
data = load_config()
prefix = data["Prefix"]
token = data["Token"]