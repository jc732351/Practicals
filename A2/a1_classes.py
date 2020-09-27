"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place

class PlaceCollection:
    """..."""
    def __init__(self):
        self.placeList=[]
        self.load_places()

    def load_places(self):
        """load places from csv file"""
        with open('places.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                p=Place(row[0],row[1],int(row[2]),row[3])
                self.placeList.append(p)

    def save_places(self):
        """save csv file"""
        f = open('places.csv', 'w',newline='')
        writer = csv.writer(f)
        for p in self.placeList:
            writer.writerow((p.name,p.country,p.priority,p.visited_status))
        f.close()

    def add_place(self,name,country,priority):
        """add places into list"""
        self.placeList.append(Place(name,country,priority,""))

    def get_num(self):
        return len([i for i in self.placeList if i.visited_status==""])

    def sort(self,key):
        """sort list"""
        if key=='priority':
            self.placeList=sorted(self.placeList,key=lambda x:x.priority,reverse=False)
        elif key=='name':
            self.placeList=sorted(self.placeList,key=lambda x:x.name,reverse=False)


