import abc


class BuildingInterface(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def createRectangle(length: int, height: int) -> str:
        pass


class Building(BuildingInterface):
    @staticmethod
    def createRectangle(length: int, height: int) -> str:
        length *= 3                                             # Fixes the aspect ratio between characters | and -
        rectangle = ("-" * length) + "\n"
        for x in range(height):
            rectangle += "| {fill: <{repeat:}} |\n".format(fill=" ", repeat=length - 4)
        rectangle += "-" * length
        return rectangle


print(Building.createRectangle(10, 5))
