import geojson
from parse import *

def create_map(data_file):
    """Creates a GeoJSON file.

    Returns a GeoJSON file that can be rendered in a GitHub
    Gist at gist.github.com.  Just copy the output file and
    paste into a new Gist, then create either a public or
    private gist.  GitHub will automatically render the GeoJSON
    file as a map.
    """

    # Define type of GeoJSON
    geo_map = {"type" : "FeatureCollection"}

    # Define empty list to collect each point to graph
    item_list = []

    # Iterate over data to create GeoJSON document
    for index, line in enumerate(data_file):

        # Skip any zero coordinates as this will throw
        # off the map
        if line["X"] == "0" or line["Y"] == "0":
            continue

        # Setup a new dictionary for each iteration
        data = {}

        # Assigne line items to appropriate GeoJSON fields
        data["type"] = "Feature"
        data["id"] = index
        data["properties"] = {"title" : line["Category"],
                              "description" : line["Descript"],
                              "date" : line["Date"]}
        data["geometry"] = {"type" : "Point",
                            "coordinates" : (line["X"], line["Y"])}

        # Add data dictionary to our item_list
        item_list.append(data)

    # For each point in our item_list, we add the point to our
    # dictionary.  setdefault creates a key called 'features' that
    # has a value type of an empty list.  With each iteration, we
    # are appending our point to that list.
    for point in item_list:
        geo_map.setdefault("features", []).append(point)

    with open("file_sf.geojson", "w") as f:
        f.write(geojson.dumps(geo_map, indent = "\t"))

def main():
    data = parse(MY_FILE, ",")

    return create_map(data)

if __name__ == "__main__":
    main()