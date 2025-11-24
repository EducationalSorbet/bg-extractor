
def print_dict(data, indent: int=0):
    for key, value in data.items():
        # Print key first
        print("\t" * indent + str(key) + ":", end=" ")

        # Print value
        if isinstance(value, dict):
            print()  # go to next line for nested dict
            print_dict(value, indent + 1)
        elif isinstance(value, list):
            print()  # go to next line for nested list
            print_list(value, indent + 1)
        elif isinstance(value, tuple):
            print()  # go to next line for nested tuple
            print_tuple(value, indent + 1)
        else:
            print(value)  # print simple value on same line


def print_list(data, indent: int=0):
    """"ONLY ABLE TO HANDLE ONE DIMENSION LIST YET"""
    
    for item in data:
        printing_as_per_type(item, indent)


def print_tuple(data, indent: int=0):
    """"ONLY ABLE TO HANDLE ONE DIMENSION TUPLE YET"""

    for item in data:
        printing_as_per_type(item, indent)

def print_as_str(data, indent: int=0, end=""):
    print(("\t"*indent) + str(data), end=end)
    

def printing_as_per_type(data, indent: int=0, end="\n"):
    
    if isinstance(data, dict):
        print_dict(data, indent)
        
    elif isinstance(data, list):
        print_list(data, indent)
    
    elif isinstance(data, tuple):
        print_tuple(data, indent)
    
    else:           # str, int, float, bool, None, etc.
        print_as_str(data, indent, end=end)
    
