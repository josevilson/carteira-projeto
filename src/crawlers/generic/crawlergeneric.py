from abc import ABC, abstractmethod

from browser.generic_browser import GenericBrowserCrawler
from tools.mongodb import MongoConnection


class AbstractCrawler(ABC):
    """
    xd
    """
    def __init__(self):
        self.browser = GenericBrowserCrawler().get_browser()
        # self.redis = RedisClient.get()
        # self.mongo = MongoConnection()

    @abstractmethod
    def crawl(self):

        pass
    
    @abstractmethod
    def execute_main(self):
        pass
    
    @abstractmethod
    def execute_before(self):
        pass
    
    @abstractmethod
    def execute_before(self):
        pass

    def get_steps(self, site):
        pass
    
    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
        except:
            raise("Não foi possível salvar os dados no Mongo")