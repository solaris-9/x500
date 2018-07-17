# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import json
import unicodecsv as csv
import time
#from aludir.items import AludirItem

class X500Pipeline(object):
    def __init__(self):
        #self.file = open('items.out', 'wb')
        self.file = open('log/X500.%s.txt' % time.strftime('%Y%m%d-%H%M%S', time.localtime()), 'wb')
        #csv.register_dialect('mycsv', delimiter='|', quoting=csv.QUOTE_NONE)
        fields = (
            'UPI',
            'Ename',
            'CSLogin',
            'Handle',
            'HRID',
            'NokiaID',
            'Email',
            'Businesstitle',
            'UserType',
            'OnNET',
            'Phone',
            'OtherPhone',
            'Mobile',
            'Assistant',
            'Fax',
            'TimeZone',
            'Company',
            'Location',
            'Building',
            'Office',
            'LocationCode',
            'CostCenter',
            'Department',
            'Organization',
            'Jobfamily',
            'Supervisor',
            'AdministratorApproval',
            'Cname',
            'Members',
        )
        self.writer = csv.DictWriter(self.file, fieldnames=fields, dialect='excel-tab')
        self.writer.writeheader()
        
    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line)
        try:
            self.writer.writerow(item)
        except Exception as e:
            print(u'####UPI: %s handling error!' % item['UPI'])
            print(e)
            
        return item

'''import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item'''