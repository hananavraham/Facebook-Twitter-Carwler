import re
from urllib.parse import urljoin
from crawler.downloader import HTMLDownloader
from crawler.models import Post, Comment
from crawler.parse.abstractions import WebsiteParserBase


class TwitterParser(WebsiteParserBase):
    def _parse_comments(self, post_id, url):
        comments_list = []
        downloader = HTMLDownloader()
        node = downloader.download(url=f'{url}/status/{post_id}')
        comments = node.find_all('div', {'class': 'js-tweet-text-container'})
        for comment in comments:
            try:
                comments_list.append([p.text for p in comment.find_all('p')])
            except Exception as ex:
                pass
        return comments_list

    def parse(self, node, url):
        if re.search('www.twitter.com', url) is not None:
            try:
                tweets = node.find_all('div', {'class': ['tweet', 'js-stream-tweet', 'js-actionable-tweet', 'js-profile-popup-actionable', 'dismissible-content']})
                parsed_tweets = []
                for tweet in tweets:
                    try:
                        #user = tweet.find('span', {'class': ['username', 'u-dir', 'u-textTruncate']}).b.text
                        parsed_tweet = {
                            #'user': user,
                            #'text': [p.text for p in tweet.find('div', {'class': 'js-tweet-text-container'}).find_all('p')],
                            #'comments': self._parse_comments(tweet['data-item-id'], url)
                            'text': tweet.find('p',{'class':'js-tweet-text'}).text,
                            'created_at':tweet.find('span',{'class':'_timestamp'}).text
                        }
                        parsed_tweets.append(parsed_tweet)
                    except Exception as e:
                        print(e)
                return parsed_tweets
            except Exception:
                return None
        return None

    def extract_targets(self, node, article, current_url):
        return []