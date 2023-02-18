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
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health = self.health - 1

    def is_alive(self):
        if self.health > 0:
            return 1
        return 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def collision_detection(x_coordinate, y_coordinate):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(alien_start_positions):
    for item in alien_start_positions:
        return (item[0], item [1])
#    for item in positions:
#        Alien.teleport(Alien, item[0], item[1])


print("------------------------------")
alien_one = Alien(5, 1)
print(alien_one.total_aliens_created)
alien_two = Alien(3, 0)
print(alien_one.total_aliens_created)
print(alien_two.total_aliens_created)
print(Alien.total_aliens_created)
alien_three = Alien(3, 0)
print(Alien.total_aliens_created)
print("------------------------------")
alien_start_positions = [(4, 7), (-1, 0)]
print(alien_start_positions)
aliens = new_aliens_collection(alien_start_positions)
print(aliens)
for alien in aliens:
    print(alien)
    print(alien.x_coordinate, alien.y_coordinate)

