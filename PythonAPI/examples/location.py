import carla

# Carla 서버에 연결
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# 월드 가져오기
world = client.get_world()

# 스펙테이터(카메라) 객체 가져오기
spectator = world.get_spectator()

# 새로운 좌표 설정
new_location = carla.Location(x=10, y=20, z=5)  # 원하는 좌표로 설정
new_rotation = carla.Rotation(pitch=-20, yaw=90, roll=0)  # 카메라 회전 설정

# 새로운 위치로 카메라 이동
spectator.set_transform(carla.Transform(new_location, new_rotation))
