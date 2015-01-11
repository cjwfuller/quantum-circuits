from abc import abstractmethod

class Gate(object):
    def __new__(cls, *args, **kwargs):
        if cls is Gate:
            raise TypeError("gate class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)

    @abstractmethod
    def get_symbol():
        pass

    @abstractmethod
    def get_matrix():
        pass

    @abstractmethod
    def get_num_qubits():
        pass
