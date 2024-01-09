import nmap  # Import the nmap module for scanning

def nmap_scan(target_ip):
    try:
        # Create an instance of PortScanner class
        nm = nmap.PortScanner()

        # Perform the scan with specified options
        nm.scan(target_ip, arguments='-p 1-1000 -O -T4')

        # Iterate through the scan data and display results
        for host in nm.all_hosts():
            print(f"Host: {host}")
            print(f"State: {nm[host].state()}")

            # Display OS information if available
            if 'osclass' in nm[host]:
                for osclass in nm[host]['osclass']:
                    print(f"OS Details: {osclass['osfamily']} - {osclass['osgen']}")

            # Display open ports and their respective services
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                ports = nm[host][proto].keys()
                for port in ports:
                    print(f"Port: {port} - State: {nm[host][proto][port]['state']} - Service: {nm[host][proto][port]['name']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    nmap_scan(target_ip)
