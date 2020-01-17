# -*- coding: utf-8 -*-
import scrapy


class PycursosSpider(scrapy.Spider):
    name = 'pycursos'
    allowed_domains = ['pycursos.com']
    start_urls = ['http://pycursos.com/']

    def parse(self, response):
        pass
