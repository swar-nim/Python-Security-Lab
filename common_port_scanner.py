import socket

def port_scan(target_host):
    try:
        # List of common ports to check
        common_ports = [21, 22, 80, 443, 3306, 3389]

        print(f"Scanning ports on {target_host}...")

        # Iterate through each port and attempt to connect
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set timeout for the connection attempt
            result = sock.connect_ex((target_host, port))

            # Check if the connection is successful (port is open)
            if result == 0:
                print(f"Port {port} open")

            sock.close()

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    target = input("Enter the target host: ")
    port_scan(target)
