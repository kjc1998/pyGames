import argparse


def build_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("height", help="grid height", type=int)
    parser.add_argument("width", help="grid width", type=int)
