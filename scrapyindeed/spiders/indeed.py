from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapyindeed.items import JobItem


class IndeedSpider(Spider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=tech%20support&l=Remote&jt=fulltime&limit=50&fromage=1']

    def parse(self, response):
        job_urls = response.xpath('//a[contains(@class, "tapItem")]/@href')
        yield from response.follow_all(job_urls, self.parse_job)

    def parse_job(self, response):
        item = JobItem()
        item['position'] = response.css('h1::text').get()
        # item['company'] = response.css('').get()
        # item['pay'] = response.css('').get()
        yield item


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(IndeedSpider)
    process.start()
