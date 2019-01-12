import logging

from crawler.crawler import Crawler
from crawler.downloader import SeleniumHTMLDownloader
from crawler.parse.facebook import FacebookParser
from crawler.parse.twitter import TwitterParser
from crawler.store import MongoItemStore
from crawler.load import MongoItemsLoader

#FACEBOOK_PAGE_TO_DOWNLOAD_FROM = 'https://www.twitter.com/search-home'
FACEBOOK_PAGE_TO_DOWNLOAD_FROM = 'https://www.facebook.com/'
def main():
    _setup_logging()
    downloader = SeleniumHTMLDownloader(r'C:\Users\hananavr\Documents\לימודים\מעבדה בין תחומית\facebookCrawler copy\crawler\chromedriver.exe')

    # mongodb://<dbuser>:<dbpassword>@ds215633.mlab.com:15633/pytheas
    store = MongoItemStore(
        host='ds215633.mlab.com',
        port='15633',
        db='pytheas',
        article_collection='hanan',
        username='pytheas',
        password='Pytheas1'
    )

    items_loader = MongoItemsLoader(
        host='ds215633.mlab.com',
        port='15633',
        db='pytheas',
        items_collection='hanan',
        username='pytheas',
        password='Pytheas1'
    )
    crawler = Crawler(downloader, {
        'www.facebook.com/': FacebookParser(),
        'www.twitter.com/': TwitterParser()
    }, store, items_loader)
    crawler.crawl(FACEBOOK_PAGE_TO_DOWNLOAD_FROM)
    

def _setup_logging():
    # create logger
    logger = logging.getLogger('crawler')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


if __name__ == '__main__':
    main()
