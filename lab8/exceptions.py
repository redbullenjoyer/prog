
class ScraperError(Exception):
    pass

class NetworkError(ScraperError):
    pass

class ParsingError(ScraperError):
    pass