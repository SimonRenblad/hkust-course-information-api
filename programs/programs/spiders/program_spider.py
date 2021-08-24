import scrapy
import re


class ProgramSpider(scrapy.Spider):
    name = "program"
    start_urls = [
        'https://prog-crs.ust.hk/ugprog/2021-22?token_post=42025789ea7b18be332277c1dd9c4721&is_s=Y&keyword=&school%5B%5D=SSCI&school%5B%5D=SENG&school%5B%5D=SBM&school%5B%5D=SHSS&school%5B%5D=IPO&career%5B%5D=req&career%5B%5D=major&career%5B%5D=BBA&career%5B%5D=BEng&career%5B%5D=BSc&career%5B%5D=EXTM-AI&career%5B%5D=dual&career%5B%5D=minor&year=2021-22&archive=',
    ]

    def parse(self, response):
        yield from response.follow_all(css='li > a[title]', callback=self.parse_pdf)
        #for link in response.css('li > a[title]'):
         #   yield scrapy.Request(link, callback=self.parse)

    def parse_pdf(self, response):
        yield {
            'files': response.css('a::attr(href)').re(r'.*\.pdf')
        }