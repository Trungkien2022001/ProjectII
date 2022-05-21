# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class VietnamnetItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    loai = Field()
    tieude = Field()
    thoigian = Field()
    doandan = Field()
    noidung = Field()
    linkanh = Field()
    tags = Field()
    tacgia = Field()
    like = Field()
    url = Field()
    