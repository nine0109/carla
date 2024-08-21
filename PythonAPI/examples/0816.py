import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.load_world('Town05') 
# world = client.get_world('Town05')

client.set_timeout(10.0)  # Increase the timeout

print(client.get_available_maps())

# Retrieve the spectator object
# spectator = world.get_spectator()


# CARLA coordinates: X 0.0, Y 0.0
spectator = world.get_spectator()
loc = carla.Location(0.0, 0.0, 500.0)
rot = carla.Rotation(pitch=-90, yaw=0.0, roll=0.0)
spectator.set_transform(carla.Transform(loc, rot))