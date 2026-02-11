from pygames.game_of_life import interactor
from typing import List


class CliController:
    def __init__(self) -> None:
        self.__interactor = interactor.Interactor()

    def dispatch_request(self, arguments: List[str]) -> None:
        pass
