import os
import glob
import shutil
import time
import sys
import re


template = open("./template.html", "r").read()


def get_invert(char):
    if char == "x":
        return "o"
    else:
        return "x"


def get_content(char):
    if char == "x":
        return """<svg fill="#efefef" height="80%" width="80%" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 460.775 460.775" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M285.08,230.397L456.218,59.27c6.076-6.077,6.076-15.911,0-21.986L423.511,4.565c-2.913-2.911-6.866-4.55-10.992-4.55 c-4.127,0-8.08,1.639-10.993,4.55l-171.138,171.14L59.25,4.565c-2.913-2.911-6.866-4.55-10.993-4.55 c-4.126,0-8.08,1.639-10.992,4.55L4.558,37.284c-6.077,6.075-6.077,15.909,0,21.986l171.138,171.128L4.575,401.505 c-6.074,6.077-6.074,15.911,0,21.986l32.709,32.719c2.911,2.911,6.865,4.55,10.992,4.55c4.127,0,8.08-1.639,10.994-4.55 l171.117-171.12l171.118,171.12c2.913,2.911,6.866,4.55,10.993,4.55c4.128,0,8.081-1.639,10.992-4.55l32.709-32.719 c6.074-6.075,6.074-15.909,0-21.986L285.08,230.397z"></path> </g></svg>"""
    elif char == "o":
        return """<svg height="80%" width="80%" xmlns="http://www.w3.org/2000/svg"><circle r="50%" cx="50%" cy="50%" fill="#efefef"></circle></svg>"""
    else:
        return ""


def check_winner(board: str, player: str = "x") -> bool:
    """
    Check if the given player (default 'x') has won the game.
    :param board: A string of 9 characters representing the Tic Tac Toe board.
    :param player: 'x' or 'o' to check for a win.
    :return: True if the given player has won, False otherwise.
    """
    if player not in {'x', 'o'}:
        raise ValueError("Player must be 'x' or 'o'.")
    
    # Replace every instance of 'x' with the given player symbol
    player_regex = re.compile(
        r"xxx[^x]{6}|[^x]{3}xxx[^x]{3}|[^x]{6}xxx|"
        r"x[^x]{2}x[^x]{2}x[^x]{2}|[^x]x[^x]{2}x[^x]{2}x[^x]|"
        r"[^x]{2}x[^x]{2}x[^x]{2}x|x[^x]{3}x[^x]{3}x|[^x]{2}x[^x]x[^x]x[^x]{2}"
    )
    
    # Replace 'x' in the regex with the player's symbol
    adjusted_regex = re.compile(player_regex.pattern.replace("x", player))
    
    return bool(adjusted_regex.search(board))


def generate_html(pattern_str):
    file = template
    has_winner_x = check_winner(pattern_str, player="x")
    has_winner_o = check_winner(pattern_str, player="o")

    winner_text = "x won!" if has_winner_x else "o won!" if has_winner_o else ""

    file = file.replace(f"id=\"winner-txt\">", f"id=\"winner-txt\">{winner_text}")

    for row in range(3):
        for col in range(3):
            idx = 2 + row * 3 + col
            char = pattern_str[idx]

            link = ""

            if char != "x" and char != "o" and not has_winner_x and not has_winner_o:
                new_pattern_str = get_invert(pattern_str[0]) + pattern_str[1:idx] + get_invert(pattern_str[0]) + pattern_str[idx + 1:]

                link = f" href=\"/{new_pattern_str}.html\""
                char = ""

            file = file.replace(f"id=\"{row}{col}\">", f"id=\"{row}{col}\"{link}>{get_content(char)}")

            with open(f"output/{pattern_str}.html", "w") as outputFile:
                outputFile.write(file)


def print_progress_bar(current, total, bar_length=40):
    progress = current / total
    block = int(bar_length * progress)
    bar = "#" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\r[{bar}] {progress * 100:.2f}% ({current}/{total})")
    sys.stdout.flush()


startTime = time.time()

if not os.path.exists("./output"):
    os.makedirs("./output")

files = glob.glob('./output/*')

dataset = open("combinations.txt", "r")

print(f"Removing old files...")

total_files = len(files)
current_file = 0

for f in files:
    os.remove(f)
    current_file += 1
    print_progress_bar(current_file, total_files)

shutil.copy("./template.css", "./output/template.css")

removeTime = time.time()

print("\nGenerating HTML files...")

lines = dataset.readlines()
total_lines = len(lines)
current_line = 0


for pattern in lines:
    #print(pattern_str)
    print_progress_bar(current_line, total_lines)
    current_line += 1
    generate_html(pattern.replace("\n", ""))

doneTime = time.time()


print(f"\nRemoving files: {removeTime - startTime}s")
print(f"Generating: {doneTime - removeTime}s")
print(f"Total: {doneTime - startTime}s")
print("Done!")
