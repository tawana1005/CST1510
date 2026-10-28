# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": [87, 120, 45], "limit": [100, 100, 100]})

df["percent"] = (df["value"] / df["limit"]) * 100   # df["percent"] creates a new column called percent

print(df)
# it shows a TypeError because the value numbers were in quotes
# i fixed by removing the quotes so that the items in value column are actually numbers and not text
# i added a print line to show the result