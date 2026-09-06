from abc import ABC,abstractmethod
class DataLoader(ABC):
    @abstractmethod
    def load(self):
        pass
class CsvLoader(DataLoader):
    def load(self):
        print("CSV File Loaded")
class Excel(DataLoader):
    def load(self):
        print("Excel File Loaded")
loaders=[CsvLoader(),Excel()]
for loader in loaders:
    loader.load();