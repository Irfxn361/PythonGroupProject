import scrapy
class NewSpider(scrapy.Spider):
     name = "new_spider"
     start_urls = ['https://brickset.com/sets/year-2004/sets/1']

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2004/index.html']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
