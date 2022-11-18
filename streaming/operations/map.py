from abc import abstractmethod

from streaming.operations.base import Operation


class MapFunction(Operation):
    """ map function class """

    def process_batch(self, events):
        """ call map function """
        return [self.map(event) for event in events]

    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__

    @abstractmethod
    def map(self, event):
        """ implements a map function

        Args:
            event (object): event object

        Returns:
            object: event object
        """
        return event
