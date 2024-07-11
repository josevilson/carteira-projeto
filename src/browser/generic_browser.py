import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class GenericBrowserCrawler:
    """
    xd
    """

    browser: None
    options = webdriver.ChromeOptions()

    default_options = [
        "--no-sandbox",
        "--disable-gpu",
        "--disable-setuid-sandbox",
        "--remote-debugging-port=9222",
        "--start-maximized"
        "--window-size=1920,1080"
        "--disable-web-security",
        "--disable-dev-shm-usage",
        "--memory-pressure-off",
        "--ignore-certificate-errors",
        "--disable-features=site-per-process",
        "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"]

    def get_browser(self, args: list[str] = None):
        """
        xd
        """
        self.service = Service("/home/dinho/.cache/selenium/chromedriver/linux64/126.0.6478.126/chromedriver")
        new_args = args
        if args is None:
            new_args = self.default_options
        self.set_options(new_args)
        return webdriver.Chrome(service=self.service, options=self.options)
    
    def is_headless(self):
        """
        xd
        """
        headless = os.getenv('HEADLESS')
        if headless is None:
            self.options.add_argument("--headless")

    def set_options(self, args: list[str] | None):
        """
        xd
        """      
        self.is_headless()
        if args:
            for arg in args:
                self.options.add_argument(arg)
