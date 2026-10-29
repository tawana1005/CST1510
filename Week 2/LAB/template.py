"""
RECORD CHECK  -  my version
===========================

Name  :  Tawananyasha Divine Kasipo
Lane  :  Cyber
Date  :  2 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

count = 0
"""User enters 3 values to be used in the report"""
label = input("Enter label (type quit to stop): ")    # input entered as text  
while label != "quit":
    used = float(input("Used:"))  # convert to float because the input intended has a numerical value  
    total = float(input("Total:"))     # total attempts made

    free = total - used  
    percent = (used / total) * 100       

    """Status of the percent, OVER LIMIT if >= 100, WARNING if >= 100 but < 100 otherwise OK"""
    if percent >= 100:
        status = "OVER LIMIT"
        count += 1      # count this record
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


    """Report showing details entered by the user: percent, difference an status of percent"""
    print("=" * 34)     # top boarder
    print(f"  RECORD CHECK   -  {label}")
    print("=" * 34)
    print(f"  Used    :  {used:>10.2f}")
    print(f"  Total   :  {total:>10.2f}")
    print(f"  Free    :  {free:>+10}") # display status from the status block
    print(f"  Percent :  {percent:>10.2f}")
    print(f"  Status  :  {status:>10}")
    print("=" * 34)   # bottom boarder

    label = input("Enter label (type quit to stop): ")  # ask user again at the end of each run until they type quit

print(f"Records over limit: {count}")     # prints once after the loop ends that's why it is not indented

