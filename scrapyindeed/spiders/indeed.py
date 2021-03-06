from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapyindeed.items import JobItem
from scrapy.utils.project import get_project_settings


class IndeedSpider(Spider):
    name = 'indeed'
    allowed_domains = ['indeed.com']

    def start_requests(self):
        job_titles = ['tech support']
        for job in job_titles:
            url = f"https://www.indeed.com/jobs?q={'%20'.join(job.split())}&l=Remote&jt=fulltime&limit=20&fromage=1"    #TODO change back to limit=50
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        job_urls = response.xpath('//a[contains(@class, "tapItem")]/@href')
        yield from response.follow_all(job_urls, self.parse_job)

        # next_page = response.xpath('//a[@aria-label="Next"]/@href').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)

    def parse_job(self, response):
        item = JobItem()
        item['title'] = response.xpath('//h1[contains(@class, "jobsearch-JobInfoHeader-title")]/text()').get()
        item['company'] = response.xpath('//div[contains(@class, "jobsearch-InlineCompanyRating")]//text()').get()
        item['stars'] = response.xpath('//meta[@itemprop="ratingValue"]/@content').get()
        item['pay'] = response.xpath('//*[@id="jobDetailsSection"]/div[2]/span/text()').get()
        item['posted'] = response.xpath('//div[@class="jobsearch-JobMetadataFooter"]/div[count(@*)=0]/text()').get()
        item['url'] = response.url
        yield item


if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(IndeedSpider)
    process.start()
