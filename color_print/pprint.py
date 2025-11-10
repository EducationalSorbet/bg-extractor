from os import system
# Support for some Not-Effective terminal color Scenarios
system("")

def pprint(text, color="default"):
    colors = {
        "default": 39,      # Default color
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37
    }
    if isinstance(color, str):
        if color not in list(colors.keys()):
            pprint(f">> Not A PreDefied Color, Selecting Deafult", "red") 
        color_code = colors.get(color, 39)
        print(f"\033[{color_code}m{text}\033[0m")
    elif isinstance(color,  int):
        print(f"\033[38;5;{color_code}m{text}\033[0m")
    else:
        raise ValueError
