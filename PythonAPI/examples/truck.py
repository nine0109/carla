# all imports
import carla
import sys

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

world = client.get_world()
spawn_points = world.get_map().get_spawn_points()

vehicle_bp = world.get_blueprint_library().filter('firetruck*')[0]
start_point = spawn_points[0]
vehicle = world.try_spawn_actor(vehicle_bp, start_point)

# get the car's position on the map
vehicle_pos = vehicle.get_transform()
print(vehicle_pos)

# inintial spawn point is the same - just 0.6m higher off the ground
print(start_point)

# send vehicle off
vehicle.set_autopilot(True)

# get actual position from the car moving
vehicle_pos = vehicle.get_transform()
print(vehicle_pos)

# now Look at the map
town_map = world.get_map()

print(town_map)

roads = town_map.get_topology()

# topoLogy is pairs of waypoints defining all roads - 
print(roads)

# making a route
# from one position to another
point_a = carla.Location(x=50.477512, y=141.135620, z=0.001844)
point_b = carla.Location(x=55.477512, y=145.135620, z=0.001844)

# import same code coming with the sim
sys.path.append('C:/Carala/pythonAPI/carla')
from agents.navigation.global_route_planner import GlobalRoutePlanner

# using the code to plan the route and then draw it in the simulator
sampling_resolution = 2

grp = GlobalRoutePlanner(town_map, sampling_resolution)
route = grp.trace_route(point_a, point_b)

for waypoint in route:
    world.debug.draw_string(waypoint[0].transform.location, '^', draw_shadow=False,
                            color=carla.Color(r=0, g=0, b=255), life_time=120.0,
                            persistent_lines=True)

# utility script of destruction
for actor in world.get_actors().filter('*vehicle*'):
    actor.destroy()

for sensor in world.get_actors().filter('*sensor*'):
    sensor.destroy()

# now we define 2 cars
truck_bp = world.get_blueprint_library().filter('*firetruck*')[0]
mini_bp = world.get_blueprint_library().filter('*cooper_s*')[0]

# start first car in already defined start point
truck = world.try_spawn_actor(truck_bp, start_point)

# tweak spectator position to watch the show
spectator = world.get_spectator()
spawn_points = world.get_map().get_spawn_points()
start_point = spawn_points[0]

spectator_pos = carla.Transform(start_point.location + carla.Location(x=20, y=10, z=10),
                                carla.Rotation(yaw=start_point.rotation.yaw - 1))
spectator.set_transform(spectator_pos)

# drop the Mini from the sky - watch what happens after
# spawn it first somewhere else
mini = world.try_spawn_actor(mini_bp, spawn_points[10])

mini_pos = carla.Transform(start_point.location + carla.Location(x=-4, z=10),
                           carla.Rotation(yaw=start_point.rotation.yaw - 0))
mini.set_transform(mini_pos)
