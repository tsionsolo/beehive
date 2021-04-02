import time
import datetime
import tempread

filename = "Beekeeping_Log.csv"

# Create header row in new CSV file
csv = open(filename, 'w')
csv.write("Timestamp             Temperature\n")
csv.close

# Initialize communication with TMP102
tempread.init()

# Sample temperature every second for 10 seconds
for t in range(0, 10):

    # Construct CSV entry from timestamp and temperature
    temp_c = str(round(tempread.read_temp(), 2))
    entry = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    entry = entry + "," + temp_f + "\n"

    # Log (append) entry into file
    csv = open(filename, 'a')
    try:
        csv.write(entry)
    finally:
        csv.close()

    # Wait 1 second before sampling temperature again
    time.sleep(1)

# When all the writing has been completed, print the CSV contents
csv = open(filename, 'r')
print(csv.read())
csv.close()
