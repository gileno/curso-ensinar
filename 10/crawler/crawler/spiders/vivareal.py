import scrapy

from scrapy_splash import SplashRequest


class VivarealSpider(scrapy.Spider):
    name = 'vivareal'
    allowed_domains = ['vivareal.com.br']
    start_urls = ['https://www.vivareal.com.br/aluguel/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/']

    def parse(self, response):
        items = response.xpath(
            '//*[@class="results-list js-results-list"]//article/div/a/@href'
        )
        for item in items.extract():
            self.log(item)
            url = response.urljoin(item)
            yield scrapy.Request(url=url, callback=self.parse_item)
        proxima_pagina = response.xpath(
            "//*[@title='Próxima página']/@data-page"
        ).extract_first()
        try:
            proxima_pagina = int(proxima_pagina)
            if proxima_pagina and proxima_pagina < 20:
                yield SplashRequest(
                    url=response.urljoin(f'?pagina={proxima_pagina}'),
                    callback=self.parse, args={'wait': 1}
                )
        except:
            pass

    def parse_item(self, response):
        item = {}
        item['preco'] = response.xpath(
            "//*[contains(@class, 'js-price-sale')]/text()"
        ).extract_first()
        item['condominio'] = response.xpath(
            "//*[contains(@class, 'js-condominium')]/text()"
        ).extract_first()
        item['area'] = response.xpath(
            "//*[contains(@class, 'js-area')]/span/text()"
        ).extract_first()
        item['quartos'] = response.xpath(
            "//*[contains(@class, 'js-bedrooms')]/span/text()"
        ).extract_first()
        item['banheiros'] = response.xpath(
            "//*[contains(@class, 'js-bathrooms')]/span/text()"
        ).extract_first()
        item['vagas'] = response.xpath(
            "//*[contains(@class, 'js-parking')]/span/text()"
        ).extract_first()
        yield item
