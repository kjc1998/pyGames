class Cell:
    """Conway Live Cell"""

    def __init__(self) -> None:
        self.__alive = False

    @property
    def is_alive(self) -> bool:
        return self.__alive

    def switch(self) -> None:
        self.__alive = not self.__alive
