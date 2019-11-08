from typing import List
import uuid

class Agregate():
    def __init__(self, name: str):
        self._name = name
        self._id = uuid.uuid4()
        self._vsets = []

    def name(self):
        """
        Name of the agregate.

        Returns:
            str: name of the agregate.
        """
        return self._name

    def set_name(self, name=''):
        """
        Set the name of the agregate.

        Args:
            name (str): name for the agregate.
        """
        _name = name

    def vsets(self):
        """
        The list of vsets.

        Returns:
            dict: The list of vsets.
        """
        return self._vsets
