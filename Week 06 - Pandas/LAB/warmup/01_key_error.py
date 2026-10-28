# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"label": ["R-001", "R-002"], "value": [87, 120], "limit": [100, 100]})

print(df["value"])
# it shows a module not found error
# i fixed by doing python -m pip install pandas then it started showing a KeyError
# i fixed by correcting the name "Value" and typing "value"