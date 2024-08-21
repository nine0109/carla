import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()

client.set_timeout(10.0)  # Increase the timeout
map = world.get_map('Town12')
print(client.get_available_maps())
