"""..."""


# Create your PlaceCollection class in this file

import csv
from place import Place

class PlaceCollection:
    """..."""

    """Initialization function, load place in it"""
    def __init__(self):
        self.placeList=[]
        self.load_places()

    """loading place from places.csv"""
    def load_places(self):
        with open('places.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                p=Place(row[0],row[1],int(row[2]),row[3])
                self.placeList.append(p)

    """save places to places"""
    def save_places(self):
        f = open('places.csv', 'w',newline='')
        writer = csv.writer(f)
        for p in self.placeList:
            writer.writerow((p.name,p.country,p.priority,p.visited_status))
        f.close()

    """add a place"""
    def add_place(self,name,country,priority):
        self.placeList.append(Place(name,country,priority,""))

    """get the number of nonvisited"""
    def get_num(self):
        return len([i for i in self.placeList if i.visited_status==""])

    """sort the places by different key"""
    def sort(self,key):
        if key=='priority':
            self.placeList=sorted(self.placeList,key=lambda x:x.priority,reverse=False)
        elif key=='name':
            self.placeList=sorted(self.placeList,key=lambda x:x.name,reverse=False)




if __name__=='__main__':
    p=PlaceCollection()
    p.load_places()
    p.save_places()
    p.sort('name')
