import re
from urllib.parse import urljoin
from crawler.models import Post, Comment
from crawler.parse.abstractions import WebsiteParserBase


class FacebookParser(WebsiteParserBase):
    def _parse_comments(self, comments):
        comments_list = []
        for comment in comments:
            try:
                user = comment.find_all('span', {'class': 'UFICommentActorName'})[0].text
                comment = comment.find('span', {'class': 'UFICommentBody'}).span.text
                comments_list.append({
                    'created_at': '',
                    'text': comment
                })
            except Exception as ex:
                try:
                    user = comment.find_all('a', {'class': 'UFICommentActorName'})[0].text
                    comment = comment.find('span', {'class': 'UFICommentBody'}).span.text
                    comments_list.append({
                        'user': user,
                        'comment': comment
                    })
                except Exception as e:
                    pass
        return comments_list

    def parse(self, node, url):
        if re.search('www.facebook.com/', url) is not None:
            try:
                #posts = node.find_all('div', {'class': ['_4-u2', '_4-u8']})
                #posts = node.find_all('div',{'class':'_6-cp'})
                #//*[@id="u_7o_2"]/div[2]/div
                posts = node.find_all('div',{'class':'_1yt'})
                parsed_posts = []
                for post in posts:
                    try:
                        parsed_post = {
                            #'user': post.find('span', {'class': ['fwb', 'fcg']}).a.text,
                            #'text': post.find('div', {'class': ['_5pbx', 'userContent _3576']}).text,
                            'text': post.find('div',{'class': '_6-cp'}).text,
                            #'likes': '',
                            #'created_at': post.find('span',{'class':'timestampContent'}),
                            'created_at': post.find('span', {'class':'_6-cm'}).a.text
                            #'comments': self._parse_comments(post.find_all('div', {'class': 'UFICommentContentBlock'}))
                        }
                        parsed_posts.append(parsed_post)
                    except Exception as e:
                        print(e)
                return parsed_posts
            except Exception:
                return None
        return None

    def extract_targets(self, node, article, current_url):
        return []


