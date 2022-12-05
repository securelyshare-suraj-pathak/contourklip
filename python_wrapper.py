import subprocess
inp1 = [[(434, 640)], [(292, 640), (144, 563), (144, 357)], [(144, 170), (270, 74), (435, 74)], [(600, 74), (726, 170), (726, 357)], [(726, 541), (604, 640), (434, 640)]]
inp2 = [[(435, 800)], [(900, 800)], [(900, -20)], [(435, -20)]]
def coords_to_string(inp):
    st = ''
    st += " ".join(str(i) for i in inp[0][0])
    for i in inp[1:]:
        st += f" {len(i)} "
        st += " ".join([" ".join(str(k) for k in j) for j in i])
    return st
s1 = coords_to_string(inp1)
s2 = coords_to_string(inp2)
s = subprocess.check_output(["./build/contourklip_example", s1, s2])
# s = subprocess.check_output(["./build/contourklip_example", "0 100 1 50 100 3 77.5 100 100 77.5 100 50 3 100 22.5 77.5 0 50 0 1 0 0", "150 25 1 100 25 3 72.3 25 50 47.3 50 75 3 50 102.5 72.3 125 100 125 1 150"])
s = s.decode()
# s.split("\n")

print(s)