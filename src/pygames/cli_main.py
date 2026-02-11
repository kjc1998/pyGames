import sys
import argparse
import enum
from pygames.game_of_life.controllers import cli_argparse as gol_argparse
from typing import List


class Game(enum.Enum):
    GAME_OF_LIFE = "game_of_life"


def parse_arguments(cli_args: List[str]) -> argparse.Namespace:
    """Argument parser for command line interactions"""
    parser = argparse.ArgumentParser(prog="PyGames")
    subparsers = parser.add_subparsers(dest="game")
    gol_parser = subparsers.add_parser(
        Game.GAME_OF_LIFE.value, formatter_class=argparse.RawTextHelpFormatter
    )
    gol_argparse.build_parser(gol_parser)

    args = parser.parse_args(cli_args)
    return args


class CliController:
    def dispatch_request(self, arguments: List[str]) -> None:
        args = parse_arguments(arguments)
        game = Game(args.game)
        print(game)


def main() -> None:
    controller = CliController()
    controller.dispatch_request(sys.argv[1:])


if __name__ == "__main__":
    main()
