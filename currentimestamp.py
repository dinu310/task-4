import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the timestamp as a string
timestamp = now.strftime("%d-%m-%y %H:%M:%S is the file created time")

# Extract the date from the timestamp
date = now.strftime("%Y-%m-%d(%H:%M:%S)")

# Create the file name with the date
filename = f"{date}.txt"

# Open the file in write mode
with open(filename, "w") as f:
    # Write the timestamp to the file
    f.write(timestamp)

print(f"File created: {filename}")
