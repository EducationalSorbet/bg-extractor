# use file pprint.py in ../color_print/
try:
    from pprint import pprint
except ImportError:
    pass

def tabular(data):
    """Print dictionary contents in Tabular format, Supports nested dicts & lists."""
    # Convert Keys and values to strings for safe length calculation
    str_keys = [str(k) for k in data.keys()]
    str_values = [str(v) for v in data.values() if not isinstance(v ,(dict, list, tuple))]

    max_key_width = int(len(max(str_keys, key=len)))
    max_value_width = int(len(max(str_values, key=len))) if str_values else 0
    
    for key, value in data.items():
        key_str = str(key)
        if isinstance(value, (list, tuple)):
            # Print list/tuple elements one per line
            try:
                pprint(f"| {key_str:<{max_key_width + 1}}:", "red", "")
            except NameError:
                print(f"| {key_str:<{max_key_width + 1}}:")
            for item in value:
                print(f"   - {item}")
        else:
            value_str = str(value)
            try:
                pprint(f"| {key_str:<{max_key_width + 1}}:", "red", "")
                pprint(f"{value_str:<{max_value_width + 1}}|", "cyan")
            except NameError:
                print(f"| {key_str:<{max_key_width + 1}}:", end="")
                print(f"{value_str:<{max_value_width + 1}}|")
            except Exception as e:
                raise Exception(f"\033[1mUnExpected Error\033[0m: {e}")


def clean_print(data):
    if isinstance(data, dict):
        tabular(data)
    else:
        print("Not Supproted Yet", type(data))
