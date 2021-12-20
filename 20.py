data = open("data/20.data").read().replace("#", "1").replace(".", "0").split("\n\n")
data[1] = data[1].split("\n")

def solve():
    def extend(image, n, symbol):
        for _ in range(n):
            image = [row.join([symbol]*2) for row in image]
            x_size = len(image[0])
            image = [symbol*x_size] + image + [symbol*x_size]
        return image

    def crop(image):
        while image[0] == image[1]:
            image = image[1:]
        while image[-2] == image[-1]:
            image = image[:-2]
        while [image[i][0] for i in range(len(image))] == [image[i][1] for i in range(len(image))]:
            image = [row[1:] for row in image]
        while [image[i][-2] for i in range(len(image))] == [image[i][-1] for i in range(len(image))]:
            image = [row[:-2] for row in image]
        return image

    def lit(image):
        return sum([sum([1 for symbol in row if symbol == "1"]) for row in image])

    def enhance(image, pixel_map, steps):
        image = extend(image, 3, "0")
        y_size = len(image)
        x_size = len(image[0])
        for _ in range(steps):
            new_image = [["0" for _ in range(x_size)] for _ in range(y_size)]
            for row in range(1, y_size - 1):
                for col in range(1, x_size - 1):
                    pixel = int("".join([image[i][j] for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)]), 2)
                    new_image[row][col] = pixel_map[pixel]
            new_image = ["".join(row[1:-1]) for row in new_image[1:-1]]
            image = crop(new_image)
            image = extend(image, 2, image[0][0])
            y_size = len(image)
            x_size = len(image[0])
        return image

    pixel_map = data[0]
    image = data[1]

    print(lit(enhance(image, pixel_map, 2)))
    print(lit(enhance(image, pixel_map, 50)))


solve()