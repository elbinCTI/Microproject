import csv
import string
import random

file=r"enc1.csv"

h=["ch"] + [str(i) for i in range(1, 64)]
ch=list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
allch = list((string.ascii_letters + string.digits + string.punctuation).replace(",", ""))
if len(allch) < len(ch):
    raise ValueError("Not enough unique characters available.")
rows=[h]


# 4. Create rows with row-labels
for c in ch:
    rows.append([c])
num_columns= len(h)
num_rows=len(rows)

for col in range(1, num_columns):  # skip column 0 ("ch"/labels)
    used = set()
    for r in range(1, num_rows):   # skip header row
        c=random.choice(allch)
        while c in used:        # ensure uniqueness per column
            c=random.choice(allch)
        used.add(c)
        rows[r].append(c)

# 6. Write to CSV
with open(file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"CSV file '{file}' created using random characters.")


