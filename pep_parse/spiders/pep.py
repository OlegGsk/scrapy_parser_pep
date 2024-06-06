import re

import scrapy

from pep_parse.constants import ALLOWED_DOMAINS, START_URLS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_links_peps = response.css(
            'section#numerical-index a::attr(href)').getall()
        for link in all_links_peps[1:]:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': self.get_pep_number(response),
            'name': self.get_pep_name(response),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        }
        yield PepParseItem(data)

    @classmethod
    def get_pep_name(cls, response):
        text = response.css('h1.page-title *::text').getall()
        name = ' '.join(text)
        return re.sub(r'PEP \d+\s–\s', '', name,)

    @classmethod
    def get_pep_number(cls, response):
        number = response.css('h1.page-title::text').get()
        return re.findall(r'\d+', number)[0]
