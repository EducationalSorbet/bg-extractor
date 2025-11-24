# use file color_print.py in ../color_print/
try:
    from color_print import pprint
except ImportError:
    pass

from clean_print import printing_as_per_type



# *args : ALLOW TO GET TUPLES AS INPUT
# **kargs : ALLOW TO GET DICT AS INPUT
def tabular_format(data):
    """Print dictionary contents in Tabular format, Supports nested dicts & lists."""
    # Convert Keys and values to strings for safe length calculation
    str_keys = [str(k) for k in data.keys()]
    str_values = [str(v) for v in data.values()]

    # max_key_width = int(max((len(k) for k in str_keys), default=0))
    max_key_width = int(max(list(map(len, str_keys)), default=0))
    max_value_width = int(max(list(map(len, str_values)), default=0))
    
    for key, value in data.items():
        key_str = str(key)
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
    """
    Unified Formatter:
    - Dicts: printed in a clean readable tree form
    - Lists/Tuples: handles multi-level nesting
    - Flat dicts printed in aligned tabular form
    """
    
    if is_flat_dict(data):
        tabular_format(data)
    else:
        printing_as_per_type(data)


def is_flat_dict(data):
    """
    Returns True if the dictionary is flat (no nested dicts or lists), False otherwise.
    """
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    for value in data.values():
        if isinstance(value, dict) or isinstance(value, list):
            return False
    return True