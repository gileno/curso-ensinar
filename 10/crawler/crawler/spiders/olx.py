# -*- coding: utf-8 -*-
import scrapy


class OlxSpider(scrapy.Spider):
    name = 'olx'
    allowed_domains = ['pe.olx.com.br']
    start_urls = ['https://pe.olx.com.br/grande-recife/recife/boa-viagem/imoveis/aluguel']

    def parse(self, response):
        items = response.xpath("//*[@id='main-ad-list']/li/a/@href")
        for item in items.extract():
            yield scrapy.Request(url=item, callback=self.parse_item)
        proxima_pagina = response.xpath(
            "//*[@rel='next']/@href"
        ).extract_first()
        if proxima_pagina:
            yield scrapy.Request(url=proxima_pagina, callback=self.parse)
    
    def parse_item(self, response):
        item = {}
        item['area'] = response.xpath(
            "//dt[contains(text(), 'Área útil')]/following-sibling::dd/text()"
        ).extract_first()
        item['quartos'] = response.xpath(
            "//dt[contains(text(), 'Quartos')]/following-sibling::a/text()"
        ).extract_first()
        item['iptu'] = response.xpath(
            "//dt[contains(text(), 'IPTU')]/following-sibling::dd/text()"
        ).extract_first()
        item['banheiros'] = response.xpath(
            "//dt[contains(text(), 'Banheiros')]/following-sibling::dd/text()"
        ).extract_first()
        item['vagas'] = response.xpath(
            "//dt[contains(text(), 'Vagas na garagem')]/following-sibling::dd/text()"
        ).extract_first()
        item['valor'] = response.xpath("//h2/text()").extract_first()
        yield item
        
