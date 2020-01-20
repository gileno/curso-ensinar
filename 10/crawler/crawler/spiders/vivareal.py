import scrapy


class VivarealSpider(scrapy.Spider):
    name = 'vivareal'
    allowed_domains = ['vivareal.com.br']
    start_urls = ['https://www.vivareal.com.br/aluguel/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/']

    def parse(self, response):
        items = response.xpath(
            '//*[@class="results-list js-results-list"]//article/div/a/@href'
        )
        for item in items.extract():
            url = response.urljoin(item)
            yield scrapy.Request(url=url, callback=self.parse_item)
        proxima_pagina = response.xpath(
            "//*[@title='Próxima página']/@data-page"
        ).extract_first()
        if proxima_pagina:
            yield scrapy.Request(
                url=response.urljoin(f'?pagina={proxima_pagina}'),
                callback=self.parse
            )

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
