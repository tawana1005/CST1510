"""
RECORD CHECK  -  my version
===========================

Name  :  Tawananyasha Divine Kasipo
Lane  :  Cyber
Date  :  23 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

class Record:
    """One record with a label, value and limit"""
    over_limit_count = 0

    def __init__(self, label, value, limit):    # defining class and creating attributes
        """Store label, value and limit"""
        self.label = label
        self.value = value
        self.limit = limit

        # class-level running total, ***I called Record (a class) and not an object
        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def status(self):
        """Return OVER LIMIT, WARNING or OK for the record"""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
        

def load_records(path):
    """Reads label, value, limit lines from a file and returns a list of Record objects"""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("tawana_record.txt")

#for r in records:
#    print(r.label, r.status())

count = 0

for r in records:
    print()
    print("=" * 34)
    print(f"  Label  -  {r.label}")
    print(f"  Value  -  {r.value}")
    print(f"  Limit  -  {r.limit}")
    print(f"  Status  -  {r.status()}")
    print("=" * 34)

    if r.status() == "OVER LIMIT":
        count += 1

print(f"Records over limit:  {count}")
print("=" * 34)


# ==========================================================================