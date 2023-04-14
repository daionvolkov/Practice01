import sys
from PIL import Image

width = 100
height = 100

input_file = "input.txt"
output_file = "output"
image_format = "PNG"

dead_point = (0, 0, 0)


def read_field():
    field = []
    with open(input_file, "r") as f:
        for line in f:
            row = []
            for c in line.strip():
                row.append(int(c))
            field.append(row)
    return field


def write_field(field):
    with open(f"{output_file}.txt", "a") as f:
        for row in field:
            for cell in row:
                f.write(str(cell))
            f.write("\n")


def convert_field_to_image(field, color):
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            if field[y][x] == 0:
                pixels[x, y] = dead_point
            else:
                age = field[y][x]
                color_tuple = tuple(int(c * age) for c in color)
                pixels[x, y] = color_tuple
    image.save(f"{output_file}.{image_format}")


def compute_next_generation(field):
    next_field = [[0 for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            neighbors = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx = (x + dx) % width
                    ny = (y + dy) % height
                    neighbors += field[ny][nx]
            if field[y][x] == 1 and (neighbors < 2 or neighbors > 3):
                next_field[y][x] = 0
            elif field[y][x] == 0 and neighbors == 3:
                next_field[y][x] = 1
            else:
                next_field[y][x] = field[y][x]
    return next_field
