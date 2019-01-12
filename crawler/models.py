class ParsedItem:
    def __init__(self, url):
        self.url = url


class MongoConfiguration:
    def __init__(self, host, port, username=None, password=None):
        self.port = port
        self.password = password
        self.username = username
        self.host = host


class Post(ParsedItem):
    def __init__(self, url, user, content, likes, comments=None):
        super().__init__(url)
        self.user = user
        self.content = content
        self.comments = comments
        self.likes = likes


class Comment(ParsedItem):
    def __init__(self, url, user, content):
        super().__init__(url)
        self.user = user
        self.content = content


