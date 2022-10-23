import scrapy
from scrapy.exceptions import DropItem

from pep_parse.constants import EN_DASH, EXPECTED_STATUS, STATUS_PEP_NOT_FOUND
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

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    def parse_pep(self, response):
        # yield {
        #     'name': response.css('.author-title::text').get().strip(),
        #     'born_date': response.css('span.author-born-date::text').get(),
        #     'born_location': response.css(
        #         'span.author-born-location::text').get()
        # }
        # number = scrapy.Field()
        # name = scrapy.Field()
        # status = scrapy.Field()
        # data = {}
        title = response.css('h1.page-title::text').get().split(EN_DASH)
        status = response.css('dt:contains("Status") + dd::text').get()
        if status in EXPECTED_STATUS:
            yield PepParseItem(
                {
                    'number': title[0][3:].strip(),
                    'name': title[1].strip(),
                    'status': status
                }
            )
        else:
            raise DropItem(
                STATUS_PEP_NOT_FOUND.format(
                    pep_link=response.url,
                    card_status=status,
                )
            )
