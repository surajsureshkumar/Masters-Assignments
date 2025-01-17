"""
CSCI-603: Assignment 6(week 6)
Author: Suraj Sureshkumar (ss7495@g.rit.edu)

This is a homework program demonstrates a rescue mission
"""
import random
import sys

from bunker import Bunker
from chopper import Chopper
from enemy_base import EnemyBase
from player import Player, Role


class Rescue_Mission:
    def __init__(self, seed: int, num_hostages: int, num_soldiers: int, num_guerrillas: int):
        """
        Constructor
        :param seed: the seed for the random number generator
        :param num_hostages: the number of hostages
        :param num_soldiers: the number of soldiers
        :param num_guerrillas: the number of guerrillas
        """
        self.rng = random.Random(seed)
        self.chopper = Chopper()
        self.bunker = Bunker(num_soldiers)
        self.enemy_base = EnemyBase(num_hostages, num_guerrillas, self.rng)
        self.predator = Player(1, Role.PREDATOR)

    def roll(self) -> int:
        """
        This function creates a random number and returns it
        :return: returns a random number
        """
        return self.rng.randint(1, 100)

    def print_stats(self) -> None:
        """
        Prints the statistics of hostages, soldiers, guerrilla remaining and the number of rescued
        :return: None
        """
        print(f'Statistics: {self.enemy_base.get_num_hostages()} hostage/s remain, '
              f'{self.bunker.get_num_soldiers()} soldier/s remain'
              f', {self.enemy_base.get_num_guerrillas()} guerrilla/s remain, {self.chopper.get_num_rescued()} rescued')

    def run_simulation(self) -> None:
        """
        Runs the rescue and do or die simulation for the hostages
        :return: None
        """
        # 1 Prints the start up message, "Get to the choppa!"
        print("Get to the choppa!")

        # 2 While the simulation is still going
        while True:
            # 3 Prints the current statistics
            self.print_stats()
            if not self.enemy_base.has_hostages() or not self.bunker.has_soldiers():
                break

            # 4 Deploying the next soldier into the enemy base to
            # attempt rescuing the next hostage
            soldier = self.bunker.deploy_next_soldier()

            hostage = self.enemy_base.rescue_hostage(soldier)

            # 5 the hostage was not rescued goto loop beginning
            if not hostage:
                continue

            # 6 prints the below message and format is used
            print(f'{hostage} rescued from enemy base by {soldier}')

            # 7 Die roll
            die = self.roll()

            # 8 prints the below message and format is used
            print(f'{soldier} encounters the predator who rolls a {die}')

            # 9  If the die roll is greater than the predator's
            # chance to defeat the soldier, declare victory of the soldier over the predator.
            # Have the hostage board the chopper, adding the soldier back to the end of the bunker, and go to while loop
            if die > Player.PREDATOR_CHANCE_TO_BEAT_SOLDIER:
                print(f'{soldier} defeats {self.predator} ')
                self.chopper.board_passenger(hostage)
                self.bunker.fortify_soldier(soldier)
                continue

            # 10 prints the below message and format is used
            print(f'{self.predator} defeats {soldier}')

            # 11 Die roll
            die = self.roll()
            print(f'{hostage} encounters the predator who rolls a {die}')  # printing the message using format

            # 12 If the die roll is greater than the predator's
            # chance to defeat the hostage, declare victory of the hostage over the predator,
            # then the hostage boards the chopper.
            if die > Player.PREDATOR_CHANCE_TO_BEAT_HOSTAGE:
                print(f'{hostage} defeats {self.predator}')
                self.chopper.board_passenger(hostage)
                continue

            # 13 prints the below message and format is used
            print(f'{self.predator} defeats {hostage}')

        # 14 soldier that may be left in the bunker
        # boards the chopper
        for i in range(self.bunker.get_num_soldiers()):
            self.chopper.board_passenger(self.bunker.deploy_next_soldier())

        # 15 rescuing remaining passengers to safety
        self.chopper.rescue_passengers()

        # 16 print statistics
        self.print_stats()


if __name__ == '__main__':
    """
        The main program
        :return: nothing
        """
    try:
        # checking if length of argument less than 5 if found returns a message
        if len(sys.argv) < 5:
            print("Usage: python rescue_mission #_seed #_hostages #_soldiers #_guerrillas")
        else:
            seed = int(sys.argv[1])
            num_hostages = int(sys.argv[2])
            num_soldiers = int(sys.argv[3])
            num_guerrillas = int(sys.argv[4])
            Rescue_Mission(seed, num_hostages, num_soldiers, num_guerrillas).run_simulation()
    except FileNotFoundError as fnfe:
        print(fnfe)
