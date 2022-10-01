import csv

with open("data/addresses.csv") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        # row is a `list`
        print(row[2])

with open("data/biostats.csv") as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
        # row is a `list`
        print(row["Name"], row["Sex"], int(row["Age"]))
