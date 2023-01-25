import scrapy
from ..items import Scrapy1Item
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        # 'https://quotes.toscrape.com/'
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata ={
            'csrf_token' : token,
            'username' : 'nepbee',
            'password' : 'nepbee123'
        }, callback=self.login)


    def login(self, response):

        open_in_browser(response)

        item = Scrapy1Item()

        all_quote_div = response.css("div.quote")

        for quote in all_quote_div:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            item['title'] = title
            item['author'] = author
            item['tag'] = tag

            yield item

        # next_page = response.css('li.next a::attr(href)').get()

        # if next_page is not None:
        #     yield response.follow(next_page,callback = self.parse)
