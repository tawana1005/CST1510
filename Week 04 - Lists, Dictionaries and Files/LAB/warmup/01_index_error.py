# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]

print(labels[2])
# it shows an indexerror because there is no index position for 3. Positions start counting at 0, so for this instance the highest position value would be 2
# to print th last item i should put the correct index which is 2