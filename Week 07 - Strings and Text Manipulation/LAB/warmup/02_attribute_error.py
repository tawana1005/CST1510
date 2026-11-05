# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value_text = "87"

cleaned = value_text.strip()
value = float(cleaned) # convert string into float
print(value)    # display the cleaned numerical value
# it shows AttributeError: 'float' object has no attribute 'strip'
# .strip() is a string method and it can not be used on float