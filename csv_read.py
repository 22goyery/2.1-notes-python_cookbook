import csv
with open("movies.cav", newline="") as file:
    reader = cav.reader(file)
    for row in reader:
        print(row[0] + "(" + str(row[1]) + ")")

