# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    """A single reord with label, value and limit"""
    def __init__(self, label, value, limit):
        """Stores the label, value and limit of the object"""
        self.label = label
        self.value = value    # stored as "amount", not "value"
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)
# showed an error at first because there was no attribute value assigned to the object
# fix by labeling self.value correctly