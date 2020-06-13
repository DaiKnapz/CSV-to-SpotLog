import sys
import csv
import datetime
from lxml import etree as ET
from pathlib import Path

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


with open(str(sys.argv[1])) as csvFilie:
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
            haul = '1' if (row[0] == "Haul") else '0'
            loco = LocoSpot(number, note, location, haul, '0', date)
            locos.append(loco)
    root = ET.Element("spotlog", version="v4.47")
    doc = ET.SubElement(root, "records")

    for loco in locos:
        ET.SubElement(doc, "record", number=loco.number, date=loco.date, location=loco.location, haul=loco.haul, hold=loco.hold)
    
    tree = ET.ElementTree(root)
    filename = Path(csvFilie.name).stem + ".xml"
    tree.write(filename, pretty_print=True)
    #print(*locos, sep = "\n\n")

