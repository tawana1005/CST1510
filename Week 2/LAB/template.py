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


sourceIP = input("Enter sourceIP- ")      
failedLogins = float(input("Enter number of failed logins:"))    
totalAttempts = float(input("Enter total attempts:"))     




difference = totalAttempts - failedLogins   
percent = (failedLogins / totalAttempts) * 100       


if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"





print("=" * 34)
print(f"  Source IP  -  {sourceIP:>18}")
print(f"  Failed logins  -  {failedLogins:>10.2f}")
print(f"  Total Attempts  -  {totalAttempts:>10.2f}")
print(f"  Status  -  {status:>10}")

print("=" * 34)
print(f"  Difference  -  {difference:>+10.2f}")
print(f"  Percent  -  {percent:>10.2f}")

print("=" * 34)
print("__end of report__")
print("_" * 34)

