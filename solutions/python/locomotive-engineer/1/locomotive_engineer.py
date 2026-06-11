"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    new_wagon_line = list(each_wagons_id[2:])

    locomotiveIndex = -1

    for index, wagon_id in enumerate(new_wagon_line):
        if wagon_id == 1:
            locomotiveIndex = index
            break

    new_wagon_line[locomotiveIndex + 1:locomotiveIndex + 1] = missing_wagons

    new_wagon_line.append(each_wagons_id[0])
    new_wagon_line.append(each_wagons_id[1])

    return new_wagon_line

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    updated_route = dict(route)

    stops = list()

    for key, value in kwargs.items():
        stops.append(value)

    updated_route["stops"] = stops

    return updated_route
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    for key, value in more_route_information.items():
        route[key] = value

    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    new_wagons = []

    for i in range(0, len(wagons_rows)):
        row = []
        
        for j in range(len(wagons_rows)):
            row.append(wagons_rows[j][i])
        
        new_wagons.append(row)

    return new_wagons
