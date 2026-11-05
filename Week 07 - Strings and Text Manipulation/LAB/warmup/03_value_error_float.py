# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)    # cut off from the other values


for piece in rest.split(","):
    key, value = piece.split("=")   # separate key and value
    try:
        print(key, float(value))    # convert value to float and print
    except ValueError:  # handle values that cannot be converted
        print("Invalid value:", value)
# it shows a ValueError: could not convert string to float: 'unknown'
# fix by using try/except