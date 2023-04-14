from func import *

field = read_field()
steps = int(sys.argv[1])
color = tuple(map(int, sys.argv[2].split(",")))
for step in range(steps):
    write_field(field)
    convert_field_to_image(field, color)
    field = compute_next_generation(field)
