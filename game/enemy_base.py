import random
from typing import Optional

from ds import Stack, Queue
from player import Player, Role


class EnemyBase:
    def __init__(self, num_hostages: int, num_guerrillas: int, rnd: random.Random):
        """
        Constructor
        :param num_hostages: number of hostages
        :param num_guerrillas: number of guerrillas
        :param rnd: random number
        """
        self.num_hostages = num_hostages
        self.num_guerrillas = num_guerrillas
        self.rnd = rnd
        self.cave = Stack()  # creating a stack for cave
        for i in range(1, num_hostages + 1):
            # pushing hostages into cave
            self.cave.push(Player(i, Role.HOSTAGE))

        self.line = Queue()  # creating a queue for line
        for i in range(1, num_guerrillas + 1):
            # adding guerrilla to line
            self.line.enqueue(Player(i, Role.GUERRILLA))

    def add_guerrilla(self, guerrilla: Player) -> None:
        """
        Add a guerrillas at the end of the cave
        :param guerrilla: the guerrilla guarding the hostage
        :return: None
        """
        self.cave.push(guerrilla)

    def add_hostage(self, hostage: Player) -> None:
        """
        adding hostage to the cave
        :param hostage: the hostage to be saved
        :return: None
        """
        self.cave.push(hostage)

    def get_guerrilla(self) -> Player:
        """
        Remove a guerrilla from the front of the line
        :return: the guerrilla at the front of the line
        """
        if self.line:
            return self.line.dequeue()

    def get_hostage(self) -> Player:
        """
        Get a hostage from the front of the cave
        :return: the hostage at the front of the cave
        """
        if self.cave:
            return self.cave.pop()

    def get_num_guerrillas(self) -> int:
        """
        Get the number of guerrillas in line
        :return: the number of guerrillas
        """
        return len(self.line)

    def get_num_hostages(self) -> int:
        """
        Get the number of hostages in the cave
        :return: the number of hostages
        """
        return len(self.cave)

    def has_hostages(self) -> bool:
        """
        Checks if cave has hostage to be rescued
        :return:  boolean value
        """
        return bool(self.cave)

    def rescue_hostage(self, soldier: Player) -> Optional[Player]:
        """
        Rescuing the hostage by sending a soldier into the enemy base
        :param soldier: soldier to rescue the hostage
        :return:
        """
        # Printing the message using format
        print(f'{soldier} enters enemy base...')

        # Removing the hostage at the front of the cave
        hostage = self.get_hostage()
        if not self.line:
            return hostage

        # Getting the next guerrilla
        guerrilla = self.line.dequeue()

        # die roll
        die = self.rnd.randint(1, 100)
        print(f'{soldier} battles {guerrilla} who rolls a {die}')
        # If the die roll is greater than the chance to defeat the soldier,
        # the soldier declares victory over the guerrilla. The front hostage
        # is then returned from the method
        if die > Player.GUERRILLA_CHANCE_TO_BEAT_SOLDIER:
            print(f'{soldier} defeats {guerrilla}')
            return hostage
        # if soldier is not victorious then guerrilla is
        print(f'{guerrilla} defeats {soldier}')
        self.cave.push(hostage)
        self.line.enqueue(guerrilla)
        return None
