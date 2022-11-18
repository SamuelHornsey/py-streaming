from abc import ABC, abstractmethod

from streaming.operations.base import Operation


class FlatMapFunction(Operation):
    """ flat map function class """

    def process_batch(self, events):
        """ call flat map function """
        batch = []
        for event in events:
            batch += self.flat_map(event)

        return batch

    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__

    @abstractmethod
    def flat_map(self, event):
        """ implements a flat map function

        Args:
            event (object): event object

        Returns:
            collection (list): list of events
        """
        return []
