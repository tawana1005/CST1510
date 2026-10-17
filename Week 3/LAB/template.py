"""
RECORD CHECK  -  my version
===========================

Name  :  Tawananyasha Divine Kasipo
Lane  :  Cyber
Date  :  9 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Returns OVER LIMIT, WARNING or OK on percent"""
    if percent>= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Returns difference and percentage as two values""" # difference between limit and value, percentage of value against limit
    difference = limit- value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Prints everything in the report"""
    print()
    print("=" * 34)
    print(f"    RECORD CHECK    -   {label}")
    print("=" * 34)
    print(f" {'Failed Logins':<15}: {value:>10.2f}")
    print(f" {'Total Logins':<15}: {limit:>10.2f}")
    print(f" {'Difference':<15}: {difference:>10.2f}")
    print(f" {'Percent':<15}: {percent:>10.2f} %")
    print(f" {'Status':<15}: {status:>10}")
    print("=" * 34)
    # <15 left align with 15 spaces to accomodate all icluding the longest line 'Failed logins'
    # remember argument will align with paramemter
   

# ==================================================================== INPUT

#sourceIP = input("Enter source IP: ")     
#failedLogins = float(input("Enter number of failed logins: "))     
#totalAttempts = float(input("Enter number of total attempts: "))    

#i observed that when i ran the code it ws asking to enter these 3 inputs twice before it proceeded
# now i have to remove this line of code since i have already included it in the loop below
      


# ================================================================== PROCESS

#difference, percent = check(failedLogins, totalAttempts)
#status = status_of(percent)
# i had to move difference, percent and status into the loop because it waas only running once and would not let me do a second run

# =================================================================== OUTPUT

#print_report(sourceIP, failedLogins, totalAttempts, difference,percent, status)

over_count = 0
while True:
    sourceIP = input("Enter source IP or quit: ")
    if sourceIP == "quit":
        break
    failedLogins = float(input("Enter number of failed logins: "))
    totalAttempts = float(input("Enter number of total attempts: "))

    difference, percent = check(failedLogins, totalAttempts)
    status = status_of(percent)

    print_report(sourceIP, failedLogins, totalAttempts, difference,percent, status)

    if status == "OVER LIMIT":  # the initial indentation here was wrong. watch out for the correct indent space
        over_count += 1

print("Records over limit= ", over_count)
print("__THANK YOU__")
print("=" * 34)





# ==========================================================================

