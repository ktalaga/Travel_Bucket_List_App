class Country:

    def __init__(self, name, picture_url, visited = False, id = None):
        self.name = name
        self.picture_url = picture_url
        self.visited = visited
        self.id = id


    def mark_visited(self):
        self.visited = True