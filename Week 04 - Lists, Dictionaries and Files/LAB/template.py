"""
RECORD CHECK  -  my version
===========================

Name  :  Tawananyasha Divine Kasipo
Lane  :  Cyber
Date  :  17 October 2026

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

def check_record(value, limit):
    """Returns difference and percentage and status of percent""" # difference between limit and value, percentage of value against limit
    difference = limit- value
    percent = (value / limit) * 100
    status = status_of(percent)
    return difference, percent, status

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

# ====================================================================== STORE

def load_records(path):
    """Read label, value, limit from a file and returns the list"""
    records = []    # creates empty list to hold the records
    with open(path) as f:
        for line in f:  # reads file one line at a time
            line = line.strip()
            if line == "":  # instruction to skip any blank lines
                continue
            label, value, limit = line.split(",")   # cuts the items into three pieces which go into label, value, limit
            value = float(value)
            limit = float(limit)
           
            r = {"label": label, "value": value, "limit": limit}    # created dictionary r
            records.append(r)   # added the dictionary to the list i.e. records
    return records    # hands the full bow back


records = load_records("records_sample.txt")

# =============================================================== PROCESS + OUTPUT

count = 0
with open("record_sample.txt", 'w') as f:
    for r in records:
        difference, percent, status = check_record(r["value"], r["limit"])
        print_report(r["label"], r["value"], r["limit"], difference, percent, status)
        f.write(f"{r['label']},{status}\n")
        if status == "OVER LIMIT":
            count += 1

print("Records over limit= ", count)

# ==========================================================================
#    FileNotFound error shows when file does not exist or if the path is not correctly input
