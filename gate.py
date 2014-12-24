from abc import abstractmethod

class Gate(object):
    @abstractmethod
    def get_symbol():
        pass

    @abstractmethod
    def get_matrix():
        pass
