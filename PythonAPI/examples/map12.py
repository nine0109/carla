import carla

client = carla.Client('localhost', 2000)
client.set_timeout(20.0)  # 타임아웃을 20초로 설정

try:
    world = client.load_world('Town12')
except RuntimeError as e:
    print(f"RuntimeError: {e}")
