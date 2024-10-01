import random
from sty import fg , rs

def generate_rgb() -> list[int, int, int]:
    red = random.randint(0, 255)
    green = random.randint(0, 255)    
    blue = random.randint(0, 255)

    return [red, green, blue]

def generate_fg_color(red:int, green:int, blue:int):
    color = fg(red, green, blue)
    return color

rgb = generate_rgb()
print(generate_fg_color(rgb[0], rgb[1], rgb[2]), 'Bonjour !', rs.fg)