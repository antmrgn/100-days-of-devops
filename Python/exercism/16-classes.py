"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    x_coordinate = 0
    y_coordinate = 0
    health = 3

    def hit():
        if Alien.health - 1 <= 0 :
            return 0
        return Alien.health - 1

    def is_alive():
        if Alien.healt > 0:
            return 1
        return 0

    def teleport(x, y):
        Alien.x_coordinate = x
        Alien.y_coordinate = y
    
    def collision_detection():
        pass

    count = 0
    def total_aliens_created():
        Alien.count += 1
        return Alien.count


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

    def new_aliens_collections():
        pass