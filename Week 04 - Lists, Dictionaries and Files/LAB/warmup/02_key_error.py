# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0, "status": "OK"}

print(record["status"])
# there is a KeyError because there is no status key in the dictionary
# i fix by defining "status" in the dictionary