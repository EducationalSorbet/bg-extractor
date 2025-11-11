# use file pprint.py in ../color_print/
try:
    from pprint import pprint
except:
    pass

def tabular(dict):
    max_key_width = int(len(max(list(dict.keys()), key=len)))
    max_value_width = int(len(max(list(dict.values()), key=len)))
    for key, value in zip(dict.keys(), dict.values()):
        try:
            pprint(f"| {key:<{max_key_width+1}}:", "red", "")
            pprint(f"{value:<{max_value_width+1}}|", "cyan")
        except NameError:
            print(f"| {key:<{max_key_width+1}}:", end="")
            print(f"{value:<{max_value_width+1}}|")
        except Exception as e:
            raise Exception(f"\033[1mUnExpected Error\033[0m: {e}")


def clean_print(data):
    if isinstance(data, dict):
        tabular(data)
    else:
        print("Not Supproted Yet", type(dict))
