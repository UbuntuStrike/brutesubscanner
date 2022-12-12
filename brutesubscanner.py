import socket
import itertools

# Replace with the target domain
target_domain = "example.com"

# Replace with the list of subdomain patterns to try
subdomain_patterns = ["www", "mail", "ftp", "*"]

# Function to generate subdomains from the given patterns
def generate_subdomains(patterns):
  for pattern in patterns:
    if pattern == "*":
      for subdomain in range(1, 100):
        yield str(subdomain) + "." + target_domain
    else:
      yield pattern + "." + target_domain

# Function to check if a host is up
def is_up(host):
  try:
    # Use the low-level socket module to connect to the host
    # on port 80 (HTTP) and check if the connection succeeds
    socket.create_connection((host, 80), timeout=1)
    return True
  except:
    return False

# Generate a list of all possible subdomains
subdomains = list(generate_subdomains(subdomain_patterns))

# Check which subdomains are up
up_subdomains = [subdomain for subdomain in subdomains if is_up(subdomain)]

# Print the list of up subdomains
print("Up subdomains:")
print(up_subdomains)

# Port scan the up subdomains
print("Scanning ports:")
for subdomain in up_subdomains:
  for port in range(1, 1024):
    # Use the low-level socket module to try connecting to the
    # specified port on the subdomain and check if the connection succeeds
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((subdomain, port))
    if result == 0:
      print(f"{subdomain}:{port} is open")
    sock.close()
