from os import system, name


def clear():
    _ = system("cls") if name == "nt" else system("clear")
