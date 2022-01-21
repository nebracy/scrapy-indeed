from scrapy import Item, Field


class JobItem(Item):
    title = Field()
    company = Field()
    stars = Field()
    pay = Field()
    posted = Field()
    url = Field()
