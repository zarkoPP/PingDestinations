import subprocess

destinations = ["google.com", "yahoo.com", "bing.com"]  # add your own list of destinations

for dest in destinations:
    result = subprocess.run(['ping', '-c', '3', dest], capture_output=True, text=True)

    if "3 received" in result.stdout:
        print(f"{dest} is reachable.")
    else:
        print(f"{dest} is unreachable.")