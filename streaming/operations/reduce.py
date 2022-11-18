from abc import abstractmethod

from streaming.operations.base import Operation


class ReducerFunction(Operation):
    """ reducer function class """

    def process_batch(self, events):
        """ call reducer """
        batch = []
        for event in events:
            key, value = event

            # attempt collect reduced
            try:
                reduced = self.storage_backend.get_key(key)
            except KeyError:
                reduced = None

            reduced = self.reduce(key, reduced, value)

            self.storage_backend.set_key(key, reduced)
            batch.append((key, reduced))

        return batch

    @property
    def type(self):
        """ return the operation type """
        return self.__class__.__base__.__name__

    @abstractmethod
    def reduce(self, key, reduced, event):
        """ abstract reducer """
        return key, event
