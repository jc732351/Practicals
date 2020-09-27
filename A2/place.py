"""..."""


# Create your Place class in this file


class Place:
    """..."""
    """the initial function ,initialize the name,country,priority,visited_status"""
    def __init__(self,name,country,priority,visited_status):
        self.name=name
        self.country=country
        self.priority=priority
        self.visited_status=""
        self.is_visited(visited_status)

    """return the information of the place"""
    def __str__(self):
        return self.name+' in '+self.country+',priority '+str(self.priority)+self.visited_status

    """Determine if you have already visited"""
    def is_visited(self,visited_status):
        if visited_status=='n':
            self.visited_status=''
        elif visited_status=='v':
            self.visited_status='(visited)'

    """set the importance of the place"""
    def is_important(self):

        if self.priority<=2:
            self.visited_status='important'