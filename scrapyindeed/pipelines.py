# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class IndeedPipeline:
    def process_item(self, item, spider):
        if item['stars'] is None:
            return item
        elif float(item['stars']) >= 3:
            return item
        else:
            raise DropItem(f"The rating of {item['company']} is too low")
