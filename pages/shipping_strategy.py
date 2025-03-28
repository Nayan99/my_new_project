from abc import ABC, abstractmethod

# интерфейс для стратегии доставки
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping(self):
        pass
