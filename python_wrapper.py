import subprocess


def coords_to_string(inp):
    st = ''
    st += " ".join(str(i) for i in inp[0][0])
    for i in inp[1:]:
        st += f" {len(i)} "
        st += " ".join([" ".join(str(k) for k in j) for j in i])
    return st


def get_coords_from_tuple_string(tup_str):
    coord_strs = tup_str[1:-1].split(") (")
    return [tuple([float(j) for j in coord_str.split(", ")]) for coord_str in coord_strs]
    
    
def get_intersction(inp1, inp2):
    s1 = coords_to_string(inp1)
    s2 = coords_to_string(inp2)
    s = subprocess.check_output(["./build/contourklip_example", s1, s2]).decode()
    remove_first_line = "\n".join(list(filter(None, s.split("\n")))[1:])
    split_by_contour = filter(None, remove_first_line.split("contour:"))
    contours_strs_unformatted = [list(filter(None, i.split("\n"))) for i in split_by_contour]
    final = [[get_coords_from_tuple_string(j) for j in i] for i in contours_strs_unformatted]
    return final


if __name__ == "__main__":
    inp1 = [[(434, 640)], [(292, 640), (144, 563), (144, 357)], [(144, 170), (270, 74), (435, 74)], [(600, 74), (726, 170), (726, 357)], [(726, 541), (604, 640), (434, 640)]]
    inp2 = [[(435, 800)], [(900, 800)], [(900, -20)], [(435, -20)]]
    print(get_intersction(inp1, inp2))
