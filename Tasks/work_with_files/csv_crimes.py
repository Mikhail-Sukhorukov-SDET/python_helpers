import csv
import collections


with open("data/Crimes.csv") as crimes:
    crimes_2015 = {}
    for row in csv.DictReader(crimes, delimiter=','):
        if "2015" in row["Date"]:
            crimes_2015[row["Primary Type"]] = crimes_2015.get(row["Primary Type"], 0) + 1
print(sorted(crimes_2015.items(), key=lambda v: v[1])[-1][0])
most_common_crime = collections.Counter(crimes_2015)
print(most_common_crime.most_common(1))
