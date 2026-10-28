# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],   # there was 3 items here
    "value": [87, 120, 90],     # there was 2 items here
})

print(df)
# it shows a ValueError because the two arrays have different length
# i fixed by adding another number on the value column
# i need to add a print line so that the result shows