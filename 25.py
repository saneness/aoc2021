data = [list(item) for item in open("data/25.data").read().split("\n")]

def solve():
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

    seafloor = data.copy()
    step = 0
    moved_east = True
    moved_south = True
    while moved_east or moved_south:
        step += 1
        seafloor, moved_east = move(seafloor, "east")
        seafloor, moved_south = move(seafloor, "south")
    
    print(step)


solve()