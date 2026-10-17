# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
with open("records.txt", "w") as f:
    f.write("records.txt")      #i fixed by creating records.txt

with open("records.txt") as f:  # the instruction if to find and open file "records.txt" under the name 'f'
    print(f.read())     #(f.read()) read contents of the file, print displays the contents

#there is an error because the location of the file is not established


