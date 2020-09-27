"""..."""


# Create your PlaceCollection class in this file

import csv
from place import Place

class PlaceCollection:
    """..."""
    def __init__(self):
        self.placeList=[]
        self.load_places()

    def load_places(self):
        with open('places.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                p=Place(row[0],row[1],row[2],row[3])
                self.placeList.append(p)

    def save_places(self):
        f = open('places.csv', 'w',newline='')
        writer = csv.writer(f)
        for p in self.placeList:
            writer.writerow((p.name,p.country,p.priority,p.visited_status))
        f.close()

    def add_place(self,name,country,priority):
        self.placeList.append(Place(name,country,priority,""))

    def get_num(self):
        return len([i for i in self.placeList if i.visited_status==""])

    def sort(self):
        a=sorted(self.placeList,key=lambda x:x.priority,reverse=False)
        for i in a:
            print(i.priority)



if __name__=='__main__':
    p=PlaceCollection()
    p.load_places()
    p.save_places()
    p.sort()