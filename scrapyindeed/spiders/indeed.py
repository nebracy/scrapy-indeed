from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapyindeed.items import JobItem


class IndeedSpider(Spider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=tech%20support&l=Remote&jt=fulltime&limit=50&fromage=1']

    def parse(self, response):
        item = JobItem()
        for url in response.xpath('//a[contains(@class, "tapItem")]/@href').getall():
            item['url'] = response.urljoin(url)
            yield item


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(IndeedSpider)
    process.start()
