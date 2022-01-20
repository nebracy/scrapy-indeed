from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyindeed.items import JobItem


class IndeedSpider(CrawlSpider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=tech%20support&l=Remote&jt=fulltime&fromage=1']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = JobItem()
        for job in response.css('div.job_seen_beacon'):
            item['position'] = job.css('span::attr(title)').get()
            yield item


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(IndeedSpider)
    process.start()
