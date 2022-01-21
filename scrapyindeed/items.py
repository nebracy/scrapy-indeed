from scrapy import Item, Field


class JobItem(Item):
    title = Field()
    company = Field()
    pay = Field()
    url = Field()
