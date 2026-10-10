# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

result = check(87, 100) # I fixed by returning the value from the function return status

print(result)
# the name status is not defined as it is created inside the function check
# there is no return so the status is checkeed but never returned. Nothing comes back

