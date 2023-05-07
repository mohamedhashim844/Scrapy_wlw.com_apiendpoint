import scrapy
import json


class ProapiSpider(scrapy.Spider):
    name = 'wlw_api'
    allowed_domains = ['wlw.de']
    start_urls = ['https://api.visable.io/unified_search/v1/companies/search?site_code=DE&q=automation&search_method=direct&city_extraction_radius=50km&page=1&sort=best&ufs_session_id=df36f3374bc7ea118cac613e37422184']

    def parse(self, response):
        data = json.loads(response.body)
        yield from data['companies']

        for i in range(2,300):
            next_page = (f'https://api.visable.io/unified_search/v1/companies/search?site_code=DE&q=automation&search_method=direct&city_extraction_radius=50km&page={i}&sort=best&ufs_session_id=df36f3374bc7ea118cac613e37422184')
            if next_page :
                yield scrapy.Request(response.urljoin(next_page),callback=self.parse,dont_filter=True)        
