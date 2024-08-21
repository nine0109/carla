import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()

client.set_timeout(10.0)  # Increase the timeout
client.load_world('Town12')
print(client.get_available_maps())

# Retrieve the spectator object
# spectator = world.get_spectator()


# CARLA coordinates: X 0.0, Y 0.0
spectator = world.get_spectator()
loc = carla.Location(0.0, 0.0, 500.0)
rot = carla.Rotation(pitch=-90, yaw=0.0, roll=0.0)
spectator.set_transform(carla.Transform(loc, rot))



# Get the location and rotation of the spectator through its transform
transform = spectator.get_transform()

location = transform.location
rotation = transform.rotation

# Set the spectator with an empty transform
spectator.set_transform(carla.Transform())
# This will set the spectator at the origin of the map, with 0 degrees
# pitch, yaw and roll - a good way to orient yourself in the map


# Get the blueprint library and filter for the vehicle blueprints
vehicle_blueprints = world.get_blueprint_library().filter('*vehicle*')

spawn_points = world.get_map().get_spawn_points()

# Spawn 50 vehicles randomly distributed throughout the map 
# for each spawn point, we choose a random vehicle from the blueprint library
for i in range(0,50):
    world.try_spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))

ego_vehicle = world.spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))


# Create a transform to place the camera on top of the vehicle
camera_init_trans = carla.Transform(carla.Location(z=1.5))

# We create the camera through a blueprint that defines its properties
camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')

# We spawn the camera and attach it to our ego vehicle
camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=ego_vehicle)


# Start camera with PyGame callback
camera.listen(lambda image: image.save_to_disk('out/%06d.png' % image.frame))


for vehicle in world.get_actors().filter('*vehicle*'):
    vehicle.set_autopilot(True)


ego_bp = world.get_blueprint_library().find('vehicle.lincoln.mkz_2020')

ego_bp.set_attribute('role_name', 'hero')

ego_vehicle = world.spawn_actor(ego_bp, random.choice(spawn_points))
