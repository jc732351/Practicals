"""..."""


# Create your Place class in this file


class Place:
    """..."""
    def __init__(self,name,country,priority,visited_status):
        self.name=name
        self.country=country
        self.priority=priority
        self.visited_status=""
        self.is_visited(visited_status)

    def __str__(self):
        return self.name+' in '+self.country+',priority '+str(self.priority)+self.visited_status

    def is_visited(self,visited_status):
        if visited_status=='n':
            self.visited_status=''
        elif visited_status=='v':
            self.visited_status='(visited)'
    def is_important(self):

        if self.priority<=2:
            self.visited_status='important'