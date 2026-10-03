# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

if value > limit:
    print("OVER")
else:
    print("OK")
# TypeError: '>' not supported betweeen instances of 'str' and 'int'
# fix: put in int() so input is numerical and not text