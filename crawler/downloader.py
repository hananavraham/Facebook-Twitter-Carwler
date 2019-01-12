import time
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver

from crawler.abstractions import HTMLDownloaderBase

SCROLL_PAUSE_TIME = 3.5
FACEBOOK_QUERY_TO_DOWNLOAD_FROM = 'https://www.facebook.com/search/top/?q=' + u"סין – סין, תאילנד – תאילנד"


class SeleniumHTMLDownloader(HTMLDownloaderBase):

    def __init__(self, webdriver_path):
        self.webdriver_path = webdriver_path
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--dns-prefetch-disable')
        self.options.add_argument('headless')

    def download(self, url):
        driver = webdriver.Chrome(self.webdriver_path, chrome_options=self.options)
        driver.get(url)
        # for Twitter search ########
        #search = driver.find_element_by_xpath('//*[@id="search-home-input"]')
        #search.send_keys("אני בשוק, אני בהלם, אני ה-מ-ו-מ-ה")
        #search_btn = driver.find_element_by_xpath('//*[@id="search-home-form"]/div[2]/button')
        #search_btn.click()
        #############################

        #for Facebook search ########
        user = driver.find_element_by_css_selector('#email')
        user.send_keys('xxxx')
        password = driver.find_element_by_css_selector('#pass')
        password.send_keys('xxxx')
        time.sleep(SCROLL_PAUSE_TIME)
        login = driver.find_element_by_css_selector('#loginbutton')
        time.sleep(7)
        login.click()
        time.sleep(7) 
        driver.get(FACEBOOK_QUERY_TO_DOWNLOAD_FROM)
        time.sleep(SCROLL_PAUSE_TIME)


        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            # trying to open tweet comments
            ##################################
            #tweets = driver.find_elements_by_class_name('js-actionCopyLinkToTweet')
            #twiits_comments = []
            #for tweet in tweets:
            #    btn = tweet.find_element_by_class_name('dropdown-link')
            #    time.sleep(6)
            #    btn.click()
            #    twiits_comments.append(driver.page_source)
            ##################################

            if new_height == last_height:
                break
            last_height = new_height
            
        
            #######################
            #commemts = driver.find_elements_by_class_name('UFIPagerLink')
            #for commemt in commemts:
            #    try:
            #        commemt.click()
            #    except Exception as e:
            #        pass
            ########################
        html = driver.page_source
        return BeautifulSoup(html, 'html.parser')


class HTMLDownloader(HTMLDownloaderBase):
    def download(self, url):
        html = request.urlopen(url).read()
        return BeautifulSoup(html, 'html.parser')


class CommentDownloader(HTMLDownloaderBase):

    def download(self, url):
        pass

    def download_with_params(self, url, params):
        pass
