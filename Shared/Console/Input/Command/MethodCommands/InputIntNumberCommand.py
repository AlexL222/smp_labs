from Shared.Console.Input import InputValue
from Shared.Command.Command import Command


class InputIntNumberCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: InputValue):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.input_int_number()
