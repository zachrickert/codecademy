"""Program to calculate vacation cost."""


def answer():
    """Return 42 always."""
    return 42


def hotel_cost(nights):
    """Return total hotel cost of $140 per night."""
    return 140.0 * nights


def plane_ride_cost(city):
    """Return the airfare for the trip."""
    city = city.lower()
    if city == "charlotte":
        plane_cost = 183.0
    elif city == "tampa":
        plane_cost = 220.0
    elif city == "pittsburgh":
        plane_cost = 222.0
    elif city == "los angeles":
        plane_cost = 475.0
    else:
        plane_cost = -1

    return plane_cost
