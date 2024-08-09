import pathlib
import sys, subprocess


def main():
    init_py = pathlib.Path(__file__)
    prg = init_py.parent.joinpath("hello-zig")
    status = subprocess.call([prg, *sys.argv[1:]])
    sys.exit(status)
