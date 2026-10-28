"""
RECORD CHECK  -  my version
===========================

Name  :  Tawananyasha Divine Kasipo
Lane  :  Cyber 
Date  :  28 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd     # tables of data

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row

# read my own CSV file into a DataFrame called df, the first line in the file becomes the name of columns
df = pd.read_csv("my_records.csv")   

# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
# percent works on the whole column at once so I dont need a loop
df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(     # apply() runs the lambda on every value in percent column
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"  # i must write the line in correct order
)

# ================================================================== OUTPUT
# 3. Print the DataFrame.
# threshold: printing the whole table including percent column
print("THE DATA FRAME")
print(df)

# typical to show only the rows that are not OK
print("=" * 44)
print("ROWS THAT ARE NOT OK")
print(df[df["status"] != "OK"])  

print("=" * 44)
print("Grouping by Status")
print(df.groupby("status").size())  
# groupby("status") splits the rows into piles by status
# .size() counts the rows
df.to_csv("records_report.csv") # means write this table into a CSV file

import matplotlib.pyplot as plt     # i need this for the chart to show, plt is like a short name
df["status"].value_counts().plot(kind="bar")
plt.title("Records by status")
plt.savefig("status_counts.png")
plt.show()
# ==========================================================================

