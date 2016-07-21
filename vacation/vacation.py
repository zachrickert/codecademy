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


def rental_car_cost(days):
    """Calculate the cost of a retal car."""
    car_cost = 40.0 * days
    if days >= 7:
        car_cost = car_cost - 50.0
    elif days >= 3:
        car_cost = car_cost - 20.0

    return car_cost
