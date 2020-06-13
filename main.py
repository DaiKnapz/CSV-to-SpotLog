import sys
import csv

class LocoSpot:
    def __init__(self, number, note, location, haul, hold, date):
        self.number = number
        self.note = note
        self.location = location
        self.haul = haul
        self.hold = hold
        self.date = date
    def __repr__(self):
        return f'Number: {self.number}\nLocation: {self.location}\nDate: {self.date}\nHaul: {self.haul}\nHold: {self.hold}'


with open('trains.csv') as csvFilie:
    csvReader = csv.reader(csvFilie, delimiter=',')
    lineCount = 0
    locos = []
    for row in csvReader:
        if lineCount == 0:
            lineCount += 1
        else:
            number = row[1]
            date = row[2]
            location = row[3]
            note = row[4]
            haul = True if (row[0] == "Haul") else False
            loco = LocoSpot(number, note, location, haul, False, date)
            locos.append(loco)
    print(*locos, sep = "\n\n")

