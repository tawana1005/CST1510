# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"
key, value = piece.split("=", 1)    # split only once, at firdt "="

# display key and value
print(key, value)
# there are 3 values so I can not assign them to 2 variable i.e. key, value
# this scenario poses a ValueError: too many values to unpack (expected to)
# the fix is to match the number of variables to the values