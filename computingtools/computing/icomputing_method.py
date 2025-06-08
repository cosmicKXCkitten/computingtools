from abc import ABC, abstractmethod


class IComputingMethod(ABC):

    @abstractmethod
    def setup_task(self):
        pass

    @abstractmethod
    def assess_sustainability(self):
        pass

    @abstractmethod
    def compute(self):
        pass