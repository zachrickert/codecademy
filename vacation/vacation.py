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
    cost = {'charlotte': 183.0,
            'tampa': 222.0,
            'pittsburgh': 222.0,
            'los angeles': 475.0}

    return cost[city]


def rental_car_cost(days):
    """Calculate the cost of a retal car."""
    car_cost = 40.0 * days
    if days >= 7:
        car_cost = car_cost - 50.0
    elif days >= 3:
        car_cost = car_cost - 20.0

    return car_cost


def trip_cost(city, days, spending_money=0):
    """Calculate the total vacation cost."""
    total = (hotel_cost(days) +
             plane_ride_cost(city) +
             rental_car_cost(days) +
             spending_money)

    return total


print (trip_cost("Los Angeles", 5, 600))
