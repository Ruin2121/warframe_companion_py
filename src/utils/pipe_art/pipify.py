from math import floor, ceil

from config import LINE_LENGTH
from src.utils.pipe_art.pipe_characters import PIPE_CHARACTERS


def pipify(text: str):
    line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8 = (
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    )
    for character in text:
        try:
            line_1 += PIPE_CHARACTERS[character][1]
            line_2 += PIPE_CHARACTERS[character][2]
            line_3 += PIPE_CHARACTERS[character][3]
            line_4 += PIPE_CHARACTERS[character][4]
            line_5 += PIPE_CHARACTERS[character][5]
            line_6 += PIPE_CHARACTERS[character][6]
            line_7 += PIPE_CHARACTERS[character][7]
            line_8 += PIPE_CHARACTERS[character][8]
        except KeyError:
            print(f"Not valid or accepted character: {character}")
    difference = LINE_LENGTH - len(line_1)
    half_dif = difference / 2
    left_space = "###" + (" " * (floor(half_dif) - 3))
    right_space = (" " * (ceil(half_dif) - 3)) + "###"
    print(left_space + line_1 + right_space)
    print(left_space + line_2 + right_space)
    print(left_space + line_3 + right_space)
    print(left_space + line_4 + right_space)
    print(left_space + line_5 + right_space)
    print(left_space + line_6 + right_space)
    print(left_space + line_7 + right_space)
    print(left_space + line_8 + right_space)
