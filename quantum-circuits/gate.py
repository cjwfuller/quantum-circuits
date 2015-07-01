"""Module includes abstract Gate class"""

from abc import abstractmethod

class Gate(object):
    """Abstract gate class

    Any gate should implement the methods here whether the gate is quantum or
    not
    """

    def __new__(cls, *args, **kwargs):
        """Prevent gate class from being instantiated"""
        if cls is Gate:
            raise TypeError("Gate class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)

    @abstractmethod
    def get_symbol(self):
        """Implementation should return gate symbol e.g. 'H' for 'Hadamard'"""
        pass

    @abstractmethod
    def get_matrix(self):
        """Implementation should return gate matrix"""
        pass

    @abstractmethod
    def get_num_qubits(self):
        """Implementation should return the number of qubits the gate acts on"""
        pass
