from aocd.models import Puzzle
from PIL import Image
import glob
import numpy as np
import os

puzzle = Puzzle(year=2021, day=25)
data = [list(item) for item in puzzle.input_data.split("\n")]

def move(seafloor, side):
    row_size = len(seafloor)
    col_size = len(seafloor[0])
    cucumbers = []
    match side:
        case "east":
            row_add = 0
            col_add = 1
            cucumber_type = ">"
        case "south":
            row_add = 1
            col_add = 0
            cucumber_type = "v"
    for row in range(row_size):
        for col in range(col_size):
            if seafloor[row][col] == cucumber_type and seafloor[(row + row_add) % row_size][(col + col_add) % col_size] == ".":
                cucumbers.append((row, col))
    for cucumber in cucumbers:
        seafloor[cucumber[0]][cucumber[1]] = "."
        seafloor[(cucumber[0] + row_add) % row_size][(cucumber[1] + col_add) % col_size] = cucumber_type
    return seafloor, len(cucumbers) != 0

def image(seafloor, step):
    colors = {
        ">": [0, 128, 128],
        "v": [128, 0, 128],
        ".": [256, 256, 256]
    }
    row_size = len(seafloor)
    col_size = len(seafloor[0])
    image = []
    for row in range(row_size):
        new_row = []
        for col in range(col_size):
            new_row.append(colors[seafloor[row][col]])
        image.append(new_row)
    if not os.path.exists("25"):
        os.makedirs("25")
    Image.fromarray(np.array(image, dtype=np.uint8), "RGB").save(f"25/{str(step).zfill(3)}.png")


seafloor = data.copy()
step = 0
moved_east = True
moved_south = True
while moved_east or moved_south:
    step += 1
    seafloor, moved_east = move(seafloor, "east")
    seafloor, moved_south = move(seafloor, "south")
    image(seafloor, step)

answer_a = step

puzzle.answer_a = answer_a

fp_in = "25/*.png"
fp_out = "25.gif"
image, *images = [Image.open(f) for f in sorted(glob.glob(fp_in))]
image.save(fp=fp_out, format="GIF", append_images=images, save_all=True, duration=100, loop=1)