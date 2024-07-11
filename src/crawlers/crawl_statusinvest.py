import time

from crawlers.generic.crawlergeneric import AbstractCrawler


class StatusInvestScraper(AbstractCrawler):
    """
    ## TODO Docstring

    Args:
        TICKET: Ação 
    """
    def __init__(self, ticket):
        super().__init__()
        self.ticket = ticket

    def crawl(self):
        self.execute_main()
        time.sleep(5)

    def execute_before(self):
        pass

    def execute_main(self):
        self.browser.get(f'https://statusinvest.com.br/acoes/{self.ticket}')
        html = self.browser.page_source
        print(html)
        time.sleep(5)
        self.browser.quit()
    
    def get_steps(self, site):
        pass


    
