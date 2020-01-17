# -*- coding: utf-8 -*-
import scrapy

# Para rodar: scrapy crawl pycursos -o videos.json

class PycursosSpider(scrapy.Spider):
    name = 'pycursos'
    allowed_domains = ['pycursos.com']
    start_urls = ['http://pycursos.com/videos/']

    def parse(self, response):
        videos = response.xpath('//*[@class="post"]/a/@href')
        for link in videos.extract():
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse_video)
        proxima_pagina = response.xpath(
            "//li[@class='next']/a/@href"
        ).extract_first()
        if proxima_pagina:
            proxima_pagina = response.urljoin(proxima_pagina)
            yield scrapy.Request(proxima_pagina, callback=self.parse)

    def parse_video(self, response):
        titulo = response.xpath("//h2/text()").extract_first()
        youtube = response.xpath(
            "//*[@class='embed-responsive embed-responsive-16by9']/iframe/@src"
        ).extract_first()
        yield {
            'titulo': titulo.strip(),
            'youtube': youtube
        }
