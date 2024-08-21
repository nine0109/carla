import psutil

def find_process_by_port(port):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            connections = proc.connections(kind='inet')
            for conn in connections:
                if conn.laddr.port == port:
                    print(f"Process ID: {proc.pid} - Name: {proc.name()}")
                    return proc.pid, proc.name()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return None, None

port_number = 2000
pid, name = find_process_by_port(port_number)

if pid:
    print(f"Process using port {port_number}: PID={pid}, Name={name}")
else:
    print(f"No process is using port {port_number}")
