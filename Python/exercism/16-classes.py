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
    

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        self.total_aliens_created = Alien.total_aliens_created + 1

    def hit(self):
        self.health = self.health - 1

    def is_alive(self):
        if self.health > 0:
            return 1
        return 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def collision_detection():
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

    def new_aliens_collections():
        pass


alien = Alien(2,0)
print(alien.x_coordinate)
print(alien.y_coordinate)
print(alien.health)
alien.hit()
alien.hit()

print(alien.health)
print(alien.is_alive())
alien.teleport(5, -4)
print(alien.x_coordinate)
print(alien.y_coordinate)
print("------------------------------")
alien_one = Alien(5, 1)
print(alien_one.total_aliens_created)
alien_two = Alien(3, 0)
print(alien_one.total_aliens_created)
print(alien_two.total_aliens_created)
print(Alien.total_aliens_created)
alien_three = Alien(3, 0)
print(Alien.total_aliens_created)