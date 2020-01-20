import scrapy


class VivarealSpider(scrapy.Spider):
    name = 'vivareal'
    allowed_domains = ['vivareal.com.br']
    start_urls = ['https://www.vivareal.com.br/aluguel/pernambuco/recife/bairros/campo-grande/apartamento_residencial/']

    def parse(self, response):
        self.log(response.xpath('//title/text()').extract_first())
