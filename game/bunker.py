from ds import Queue
from player import Player, Role


class Bunker:
    def __init__(self, num_of_soldiers: int):
        """
        Constructor
        :param num_of_soldiers: the number of soldiers
        """
        self.num_of_soldiers = num_of_soldiers
        self.bunker = Queue()
        # Each soldier will be created with an id ranging between 1 and num_soldiers
        for soldier_id in range(1, num_of_soldiers + 1):
            self.bunker.enqueue(Player(soldier_id, Role.SOLDIER))

    def deploy_next_soldier(self) -> Player:
        """
        Deploys the next soldier to enemy base
        :return: Player
        """
        if self.bunker:
            return self.bunker.dequeue()

    def fortify_soldier(self, soldier: Player) -> None:
        """
        Pushing soldiers to bunker
        :param soldier: the soldier
        :return: None
        """
        self.bunker.enqueue(soldier)

    def get_num_soldiers(self) -> int:
        """
        Getting the number of soldiers
        :return: int
        """
        return len(self.bunker)

    def has_soldiers(self) -> bool:
        """
        Checking if soldiers are present
        :return: boolean value
        """
        return not self.bunker.is_empty()
