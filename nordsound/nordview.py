import argparse

from .NordSoundLoader import NordSoundLoader
from .logger import info

def run():
    parser = argparse.ArgumentParser(description='Display Nord Sound File parameters.')
    parser.add_argument('files', nargs='*', help='Files')
    args = parser.parse_args()
    for file in args.files:
        sound = NordSoundLoader().load(file)
        info(sound)
