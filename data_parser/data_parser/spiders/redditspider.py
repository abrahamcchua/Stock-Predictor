import scrapy

class RedditSpider(scrapy.Spider):
    name = 'stock'
    start_urls = ['https://www.reddit.com/r/stocks/top/?t=week']
    
    
    def parse(self, response):
        for post in response.css("div._1oQyIsiPHYt6nx7VOmd1sz"):
            yield {
            'datetime': post.css("span._2VF2J19pUIMSLJFky-7PEI::text").get(),
            'title': post.css("h3._eYtD2XCVieq6emjKBH3m::text").get(),
            'content': post.css('p._1qeIAgB0cPwnLhDF9XSiJM::text').getall(),
            'upvotes': post.css("div._1rZYMD_4xY3gRcSS3p8ODO::text").get(),
            'link': "https://www.reddit.com"+ post.css("a._2INHSNB8V5eaWp4P0rY_mE").attrib['href']
            }