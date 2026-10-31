# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    """a record than can report a status"""
    def status(self, percent):    # this parameter should be self
        """Return the percent"""
        return percent

r = Record()
print(r.status(95))
