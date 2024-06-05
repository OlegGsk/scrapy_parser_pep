import scrapy
from pep_parse.items import PepParseItem
import re


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_links_peps = response.css(
            'section#numerical-index a::attr(href)').getall()
        for link in all_links_peps:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': re.findall(r'\d+', response.url)[0].lstrip('0'),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        }
        yield PepParseItem(data)
