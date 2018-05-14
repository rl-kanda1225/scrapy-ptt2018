# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PttPipeline(object):


'''     def process_item(self, item, spider):
      return item '''

    def open_spider(self, spider):
        self.file = codecs.open('test.json', 'w', encoding='utf-8')  # 重要2

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 重要3
        self.file.write(line)
        return item
