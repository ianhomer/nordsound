import argparse

from .NordSoundLoader import NordSoundLoader
from .logger import debug

def run():
    parser = argparse.ArgumentParser(description='Display Nord Sound File parameters.')
    parser.add_argument('files', nargs='*', help='Files')
    args = parser.parse_args()
    sound = NordSoundLoader().load(args.files[0])
    debug(sound)
