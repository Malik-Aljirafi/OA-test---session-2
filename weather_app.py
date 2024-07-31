# weather app

from abc import ABC, abstractmethod

class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self, url: str) -> dict:
        pass

class WeatherProcessor:
    def extract_temp(self, data: dict) -> int:
        pass

    def extract_humidity(self, data: dict) -> int:
        pass

class WeatherApp:
    def __init__(self, data_fetcher: DataFetcher):
        self.data_fetcher = data_fetcher
        self.processor = WeatherProcessor()

    def get_weather(self, city: str) -> dict:
        pass

class WebDataFetcher(DataFetcher):
    def fetch_data(self, url: str) -> dict:
        pass


