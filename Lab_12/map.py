class Map:

    """Represents a Map class
    Attributes:
    map (list): 2d list of the map
    reveal (bool): X markers on the map for each string in the text file
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args):
        """Is a singleton decorator"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initializes the map and loads it"""
        if not Map._initialized:
            Map._initialized = True
            self.load_map(1)

    def __getitem__(self, row):
        """Returns the row on the map"""
        return self._map[row]
    
    def __len__(self):
        """Returns the length of the string of the map"""
        return len(self._map)

    def show_map(self, loc):
        """Returns the map in a 2D grid"""
        map_string = ""
        for i in range(len(self._reveal)):
            for j in range(len(self._reveal[0])):
                if loc[0] == i and loc[1] == j:
                    map_string += "* "
                elif not self._reveal[i][j]:
                    map_string += "x "
                elif self._reveal[i][j]:
                    map_string += (self._map[i][j] + " ")
            map_string += "\n"
        return map_string

    def reveal(self, loc):
        """Reveals the letter at the location of the object"""
        self._reveal[loc[0]][loc[1]] = True

    def remove_at_loc(self, loc):
        """Replaces the letter at the location with 'n'"""
        self._map[loc[0]][loc[1]] = 'n'

    def load_map(self, map_num):
        """Reads the text file and reads it"""
        self._map = []
        file_name = f"Lab_12//map{map_num}.txt"
        with open(file_name, 'r') as file:
                for text in file:
                    text = text.strip()
                    self._map.append(list(text))
        self._reveal = [[False for i in range(len(self._map))] for i in range(len(self._map[0]))]

if __name__ == "__main__":
    mapA = Map()
    print(mapA[0][0])
    print(len(mapA[0][2]))
    mapA.load_map(3)
    mapA._reveal[0][0] = True
    mapA._reveal[1][1] = True
    print(mapA.show_map([1,3]))