from os import system
# Support for some Not-Effective terminal color Scenarios
system("")

Asci_end = "\033[0m"

def pprint(text, color="default", end_with="\n"):
    """Print colored text safely in most terminals."""
    colors = {
    	"bold": 1,
        "default": 39,      # Default color
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37
    }

    # Handle string color names
    if isinstance(color, str):
        if color not in colors:
            # Avoid recusive pprint() call here (it could loop)
            pprint(f">> Not A PreDefied Color, Selecting Deafult", "red") 
        color_code = colors.get(color, 39)
        print(f"\033[{color_code}m{text}\033[0m", end=end_with)
    elif isinstance(color,  int):
        print(f"\033[38;5;{color}m{text}\033[0m", end=end_with)
    else:
        raise ValueError
