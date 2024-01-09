import socket  # Importing the socket module for network-related operations
from urllib.parse import urlparse  # Importing urlparse to extract hostname from URL

def get_ip_address(url):
    try:
        parsed_url = urlparse(url)
        # Extract the hostname from the parsed URL
        hostname = parsed_url.hostname
        if hostname:
            # Use socket.gethostbyname() to retrieve the IP address of the hostname
            ip_address = socket.gethostbyname(hostname)
            return ip_address  # Return the obtained IP address
        else:
            return "Invalid URL: No hostname found"
    except socket.error as e:
        return f"Error: {e}"  # Return an error message in case of an exception

# Get the URL from the user
url = input("Enter the website URL starting with 'https://': ")

# Retrieve and display the IP address
ip_address = get_ip_address(url)  # Call the function to get the IP address
print(f"The IP address of {url} is: {ip_address}")  # Display the IP address to the user
