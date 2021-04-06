class Sight:

    def __init__(self, name, picture_url, city, visited = False, id = None):
        self.name = name
        self.picture_url = picture_url
        self.city = city
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True