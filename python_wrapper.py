import subprocess
s = subprocess.check_output(["./build/contourklip_example", "0 100 1 50 100 3 77.5 100 100 77.5 100 50 3 100 22.5 77.5 0 50 0 1 0 0", "150 25 1 100 25 3 72.3 25 50 47.3 50 75 3 50 102.5 72.3 125 100 125 1 150"])
s = s.decode()
print(s)