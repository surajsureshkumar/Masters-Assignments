import enum


class Role(enum.Enum):
    """
    Enum class
    """
    PREDATOR = 1
    HOSTAGE = 3
    SOLDIER = 2
    GUERRILLA = 4

    def __str__(self):
        """
        Str method
        :return: returns self.name
        """
        return self.name


class Player:
    # Below are the additional attributes
    GUERRILLA_CHANCE_TO_BEAT_SOLDIER = 20
    PREDATOR_CHANCE_TO_BEAT_HOSTAGE = 75
    PREDATOR_CHANCE_TO_BEAT_SOLDIER = 50

    __slots__ = ("player_id", "role",)
    role_types = ["Soldier", "Guerrilla", "Hostage", "Predator"]  # role types

    def __init__(self, player_id: int, role: Role):
        """
        Constructor
        :param player_id: the player id
        :param role: the role of the player
        """
        self.player_id = player_id
        self.role = role

    def __str__(self):
        """
        Str method
        :return: role and player id
        """
        return f'{self.role} #{self.player_id}'

    def print_victory_message(self, opponent: 'Player'):
        """
        printing the victory message
        :param opponent: the player
        :return: None
        """
        print(f'{self} defeats {opponent}')
