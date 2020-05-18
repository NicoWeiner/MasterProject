from bs4 import BeautifulSoup
import requests
# from selenium import webdriver


# returns number of resultpages
def getNumOfPages(soup):
    return len(soup.find_all("option"))


## return BS object
def configBS(url):
    ## download website
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


# def createHeadlessFirefoxBrowser():
#     options = webdriver.FirefoxOptions()
#     options.add_argument('--headless')
#     return webdriver.Firefox(options=options)


# def configBS(url):
#     ## download website
#     browser = createHeadlessFirefoxBrowser()
#     page = browser.get(url)
#     # page = browser.page_source

#     return BeautifulSoup(page, "html.parser")

