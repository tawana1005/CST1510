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

# input source IP is a text input 
# failed logins and total attempts are numerical values input as float to allow user to enter decimal number

sourceIP = input("Enter source IP: ")     
failedLogins = float(input("Enter number of failed logins: "))     
totalAttempts = float(input("Enter number of total attempts: "))    


#

difference = totalAttempts - failedLogins   # calculates difference using values entered by user
percent = failedLogins /  totalAttempts * 100     #


# print: to show output of the input and calculations enterered
# difference and percent must be right aligned i.e.  :>10.2f    where > shows direction of alignment,
# 10 is the number of characters of the spaces and .2 means exactly 2 decimal places

print()
print("=" * 34)
print(f"  sourceIP is:  {sourceIP}")
print(f"  Number of failed logins=  {failedLogins}")
print(f"  Number of attempts=  {totalAttempts}")
print("=" * 34)

print(f"Difference:  {difference:>+10.2f}")
print(f"Percent:   {percent:>10.2f}")

print("RECORD CHECK" , sourceIP, "COMPLETE")

print("=" * 34)


