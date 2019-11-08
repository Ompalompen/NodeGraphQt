import Agregate
from typing import List
import uuid

class Group():
    def __init__(self, name: str):
        self._name = name
        self._id = uuid.uuid4()
        self._agregates : List[Agregate] = []


    def id(self):
        """
        ID of the group.

        Returns:
            str: ID of the group.
        """
        return self._id.__str__

    def name(self):
        """
        Name of the group.

        Returns:
            str: name of the group.
        """
        return self._name

    def set_name(self, name=''):
        """
        Set the name of the group.

        Args:
            name (str): name for the group.
        """
        _name = name

    def agregates(self):
        """
        The list of agregates.

        Returns:
            dict: the list of agregates.
        """
        return self._agregates