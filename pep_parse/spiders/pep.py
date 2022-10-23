import re

import scrapy

from pep_parse.constants import EXPECTED_STATUS, PATTERN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.css('#numerical-index tbody tr')
        for pep_link in all_pep:
            yield response.follow(
                pep_link.css('a.pep.reference.internal')[0],
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        title_match = re.search(
            PATTERN,
            response.css('h1.page-title::text').get()
        )
        status = response.css('dt:contains("Status") + dd::text').get()
        if status in EXPECTED_STATUS:
            yield PepParseItem(
                {
                    'number': title_match.group('number'),
                    'name': title_match.group('name'),
                    'status': status
                }
            )
