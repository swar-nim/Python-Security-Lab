import socket
import struct
import subprocess

# Get the IP address from the user
ip_address = input("Enter the IP address of the remote system: ")

# Check if the IP address is valid
try:
    socket.inet_aton(ip_address)
except socket.error:
    print("The IP address you provided is not valid! Exiting program.")
    exit()

# Check if the IP address exists
if not socket.gethostbyaddr(ip_address):
    print("The IP address you provided does not exist! Exiting program.")
    exit()

# Set the most commonly used ports
common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 119, 143, 443, 3389]

# Create an empty list to store the open ports
open_ports = []

# Scan for open ports
for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip_address, port))
    if result == 0:
        open_ports.append(port)
    sock.close()

# Display the open ports and services used
for port in open_ports:
    try:
        service = socket.getservbyport(port)
    except socket.error:
        service = "Unknown service"
    print(f"Port {port} is open, using service {service}.")

# Ask the user if they want to save the results
save_results = input("Do you want to save the results to a text file? (yes/no): ")

# Keep asking the user until they enter a valid answer
while save_results.lower() not in ("yes", "no", "y", "n"):
    save_results = input("Please provide a valid answer (yes/no): ")

# Check if the user wants to save the results
if save_results.lower() in ("yes", "y"):
    # Create a text file
    with open("open_ports.txt", "w") as open_ports_file:
        # Get the version of the services used
        for port in open_ports:
            try:
                service = socket.getservbyport(port)
            except socket.error:
                service = "Unknown service"
            try: 
                version_command = f"nmap -sV -p {port} {ip_address}"
                output = subprocess.check_output(version_command, shell=True).decode()
                version = output.split()[4]
            except:
                version = "Unknown version"
            # Add the port and service details to the file
            open_ports_file.write(f"Port {port} is open, using service {service} (version {version}).\n")
    print("Results saved to open_ports.txt file!")
