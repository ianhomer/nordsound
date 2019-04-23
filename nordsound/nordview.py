import argparse

from .NordSound import NordSound
from .logger import debug

def run():
    parser = argparse.ArgumentParser(description='Display Nord Sound File parameters.')
    parser.add_argument('files', nargs='*', help='Files')
    args = parser.parse_args()
    sound = NordSound().load(args.files[0])
    debug(sound)
