import geopandas as gpd
from shapely.geometry import Point
import random


# URL to the map from Swisstopo
MAP_URL = "https://map.geo.admin.ch/?lang=en&crosshair=marker"
# https://map.geo.admin.ch/?lang=en&crosshair=marker&zoom=7&E=2716811.14&N=1078706.29
map_zoom = 7


# Generates a (random) set of coordinates within the borders of Switzerland and/or checks if they are in the country.
class SwissRandom:
    def __init__(self, coordinate_e: float = 0, coordinate_n: float = 0):
        # Bounding boxes of Switzerland (and Liechtenstein) in LV95, LV03, and WGS84
        self.coord_boxes = {
            "LV95": {
                "min_e": 2485410,
                "min_n": 1075269,
                "max_e": 2833859,
                "max_n": 1295934,
            },
            "LV03": {
                "min_e": 485411,
                "min_n": 75271,
                "max_e": 833858,
                "max_n": 295934,
            },
            "WGS84": {
                "min_e": 5.95590,
                "min_n": 45.81796,
                "max_e": 10.49219,
                "max_n": 47.80845,
            },
        }

        # Read the shape file
        self.shape_ch = gpd.read_file("data/swissBOUNDARIES3D_1_5_TLM_LANDESGEBIET.shp")

        self.set_coord_system("LV95")
        self.coordinate_e = coordinate_e
        self.coordinate_n = coordinate_n

    def __str__(self) -> str:
        return f"{self.__coord_system}: {self.coordinate_e}, {self.coordinate_n}"

    # Set the coordinate system
    def set_coord_system(self, coord_system: str):
        if coord_system == "" or coord_system is None:
            self.__coord_system = "LV95"
        # elif coord_system in self.coord_boxes.keys():
        #     self.__coord_system = coord_system
        if coord_system.upper() == "LV95":
            self.__coord_system = coord_system.upper()
        else:
            raise ValueError(
                f"Coordinate system {coord_system} is not supported. Use one of {self.coord_boxes.keys()}"
            )

    # Get the coordinate system
    def get_coord_system(self) -> str:
        return self.__coord_system

    # Get the bounding box of the coordinate system
    def get_coord_box(self) -> dict:
        return self.coord_boxes[self.__coord_system]

    # Get the east coordinate
    def get_coord_east(self) -> float:
        return self.coordinate_e

    # Get the north coordinate
    def get_coord_north(self) -> float:
        return self.coordinate_n

    # Get the coordinates
    def get_coords(self) -> tuple:
        return (self.coordinate_e, self.coordinate_n)

    # Get random coordinates within the bounding box of the coordinate system
    def generate_coords(self):
        # Generate random east coordinates
        self.coordinate_e = random.uniform(
            self.coord_boxes[self.__coord_system]["min_e"],
            self.coord_boxes[self.__coord_system]["max_e"],
        )
        # Generate random north coordinates
        self.coordinate_n = random.uniform(
            self.coord_boxes[self.__coord_system]["min_n"],
            self.coord_boxes[self.__coord_system]["max_n"],
        )

        # Check if both coordinates are within CH or FL
        if self.check_coords():
            return (self.coordinate_e, self.coordinate_n)
        else:
            self.generate_coords()

    # Check if the coordinates are within Switzerland (or Liechtenstein)
    def check_coords(self) -> bool:
        point = Point(float(self.coordinate_e), float(self.coordinate_n))
        # Check if the point is within the shape file
        if any(self.shape_ch.contains(point)):
            return True
        else:
            return False

    def get_map_url(self):
        return f"{MAP_URL}&zoom={map_zoom}&E={self.coordinate_e}&N={self.coordinate_n}"


if __name__ == "__main__":
    # Create an instance of the class
    sr = SwissRandom()

    # Generate some random coordinates
    print(
        "Generate some random coordinates\nTravelling back and forth across Switzerland . . ."
    )
    coords = []
    for c in range(1000):
        sr.generate_coords()  # Generate random coordinates
        coords.append(sr.get_coords())  # Get the coordinates

    # Print the most and least coordinates of the generated coordinates
    northernmost = max(coords, key=lambda x: x[1])
    print(
        "northernmost",
        northernmost,
        f"{MAP_URL}&zoom={map_zoom}&E={northernmost[0]}&N={northernmost[1]}",
    )

    easternmost = max(coords, key=lambda x: x[0])
    print(
        "easternmost",
        easternmost,
        f"{MAP_URL}&zoom={map_zoom}&E={easternmost[0]}&N={easternmost[1]}",
    )

    southernmost = min(coords, key=lambda x: x[1])
    print(
        "southernmost",
        southernmost,
        f"{MAP_URL}&zoom={map_zoom}&E={southernmost[0]}&N={southernmost[1]}",
    )

    westernmost = min(coords, key=lambda x: x[0])
    print(
        "westernmost",
        westernmost,
        f"{MAP_URL}&zoom={map_zoom}&E={westernmost[0]}&N={westernmost[1]}",
    )
