"""
RECORD CHECK  -  my version
===========================

Name  :  Tawananyasha Divine Kasipo
Lane  :  Cyber
Date  :  04 Novmber 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. 
def parse_line(raw_line):
    """Cleans and parses one raw, messy line into a dict"""
    line = raw_line.strip() # removing spaces from both ends
    record = {}    

    for piece in line.split(","):   # one key=value piece at a time
        key, value = piece.split("=")   # cut at the =
        key = key.strip().lower()   # cleans the key, removes spaces and makes it lowercase
        value = value.strip()   # cleans the value, no need for .lower() because value is numbers

        if key == "attempts":
            value = int(value)
        else:
            value = value.lower()

        record[key] = value

    return record   # hands back the new finished dict

#def status_of():
    """Returns OVER LIMIT, WARNING or OK of a given record"""
    percent = record["used"] / record["total"]
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 100:
        return "WARNING"
    else:
        return "OK"

def status_of(records):
    """Returns FLAGGED if the login failed 5 times or more, otherwise OK"""
    if record["result"] == "failed" and record["attempts"] >= 5:    # both conditions must be satisfied
        return "FLAGGED"
    else:
        return "OK"

# ====================================================================== INPUT
# 2.
def load_raw_records(path):
    """Reads a text file a returns list of raw strings"""
    raw_records = []    # start with an empty list
    with open(path) as f:   # open the file
        for line in f:      # one line at a time
            if line.strip() != "":  # skip blank lines
                raw_records.append(line)    # keep the raw messy line
        return raw_records  # after the whole file is read

raw_records = load_raw_records("raw_records.txt")   # loading input from a while
# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.

record_count = 0    # how many records have been processed
flagged_count = 0   # how many were flagged

for raw_record in raw_records:      # one raw line at a time
    try:
        record = parse_line(raw_record)
    except ValueError:  # for example, int("many") raises ValueError
        print("Could not parse:", raw_record.strip())   # report the bad line, 
        continue        # skip the bad line and go to the next record

    status = status_of(record)  # FLAGGED or OK
    print(record, status)       # show the dict and its status together

    record_count += 1
    if status == "FLAGGED": # only count FLAGGED records
        flagged_count += 1

print(f"{record_count} records, {flagged_count} flagged")   #   summary once after the loop


# ==========================================================================


