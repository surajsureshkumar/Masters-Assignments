from ds import Stack


class Chopper:
    MAX_OCCUPANCY = 6

    def __init__(self):
        """
        Constructor
        """
        self.chopper = Stack()
        self.rescued = 0  # initializing rescued to 0

    def board_passenger(self, player) -> None:
        """
        Boards the passenger onto the chopper
        :param player: player refers to hostage and soldier
        :return:
        """
        self.chopper.push(player)
        print(f'{player} boards the chopper!')

        # checking if full
        if self.is_full():
            self.rescue_passengers()

    def get_num_rescued(self) -> int:
        """
        Getting the number of rescued
        :return: the number of resuced
        """
        return self.rescued

    def is_empty(self) -> bool:
        """
        Checking if chopper is empty
        :return: boolean value
        """
        return bool(self.chopper)

    def is_full(self) -> bool:
        """
        Check if the chopper is full
        :return:  a boolean value
        """
        return len(self.chopper) == Chopper.MAX_OCCUPANCY

    def rescue_passengers(self) -> None:
        """
        rescuing the passenger and dropping them to safety
        :return:
        """
        self.rescued += len(self.chopper)  # counting directly the number of people rescued
        while self.chopper:
            print(f'Chopper transported {self.chopper.pop()} to safety!')
