# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def status_of(percent, warning_at=90): # fix- putting a default value
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95)) # 95 is for percent but warning_at is undefined
# the function is defined with two parameters percent and warning_at.
# both values are required for the code to run
