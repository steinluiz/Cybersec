import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_boxed(lines):
    max_len = max(len(line) for line in lines)
    print("╔" + "═" * (max_len + 2) + "╗")
    for line in lines:
        print(f"║ {line.ljust(max_len)} ║")
    print("╚" + "═" * (max_len + 2) + "╝")