"""(Incomplete) Tests for Place class."""

from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    # print("Test empty place:")
    # default_place = Place()
    # print(default_place)
    # assert default_place.name == ""
    # assert default_place.country == ""
    # assert default_place.priority == 0
    # assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    # add_place = Place("Malagar", "Spain", 1, "")

    # TODO: Write tests to show this initialisation works

    print("Test initial-value place:")
    p=Place("Malagar", "Spain", 1, "")

    # TODO: Add more tests, as appropriate, for each method

    """test unvisited places"""

    print(p.visited_status)

    """test visited places"""
    p.is_visited('v')
    print(p.visited_status)


    """test important place"""
    p.is_important()
    print(p.visited_status)

run_tests()
