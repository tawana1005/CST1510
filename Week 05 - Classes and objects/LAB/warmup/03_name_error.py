# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, value, limit):
        """Stores the label, value and limit of the object"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns OVER LIMIT or OK on value"""
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)
print(r.status())
# name 'status' must be defined
# fixed by defining status by calling object r i.e. r.status

