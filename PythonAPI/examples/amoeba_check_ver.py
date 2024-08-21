import carla

# Carla 클라이언트에 연결
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# 클라이언트 버전 확인
client_version = client.get_client_version()
print(f"Client API version: {client_version}")

# 서버 버전 확인
server_version = client.get_server_version()
print(f"Simulator API version: {server_version}")

# 버전 비교
if client_version == server_version:
    print("Client and Server versions match.")
else:
    print("WARNING: Client and Server versions do not match.")
