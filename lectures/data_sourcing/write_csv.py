import csv

beatles = [
    {"first_name": "John", "last_name": "lennon", "instrument": "guitar"},
    {"first_name": "Ringo", "last_name": "Starr", "instrument": "drums"},
]

with open("data/beatles.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    writer.writeheader()
    for beatle in beatles:
        writer.writerow(beatle)
