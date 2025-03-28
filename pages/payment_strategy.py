from abc import ABC, abstractmethod

# интерфейс для стратегии оплаты
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
