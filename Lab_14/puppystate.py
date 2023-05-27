import abc

class PuppyState(abc.ABC):

    @abc.abstractclassmethod
    def plays(self, puppy):
        pass

    @abc.abstractclassmethod
    def feeds(self, puppy):
        pass