from scrapy import Item, Field


class JobItem(Item):
    position = Field()
    company = Field()
    pay = Field()
    url = Field()
