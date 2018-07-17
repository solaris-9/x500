# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class X500Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    UPI  =  scrapy.Field()
    Ename  =  scrapy.Field()
    CSLogin  =  scrapy.Field()
    Handle  =  scrapy.Field()
    HRID  =  scrapy.Field()
    NokiaID = scrapy.Field()
    Email  =  scrapy.Field()
    Businesstitle  =  scrapy.Field()
    UserType  =  scrapy.Field()
    OnNET  =  scrapy.Field()
    Phone  =  scrapy.Field()
    OtherPhone  =  scrapy.Field()
    Mobile  =  scrapy.Field()
    Assistant  =  scrapy.Field()
    #Fax  =  scrapy.Field()
    #TimeZone  =  scrapy.Field()
    Company  =  scrapy.Field()
    Location  =  scrapy.Field()
    Building  =  scrapy.Field()
    Office  =  scrapy.Field()
    LocationCode  =  scrapy.Field()
    CostCenter  =  scrapy.Field()
    Department  =  scrapy.Field()
    Organization  =  scrapy.Field()
    Jobfamily  =  scrapy.Field()
    Supervisor  =  scrapy.Field()
    AdministratorApproval  =  scrapy.Field()
    Cname  =  scrapy.Field()
    Members  =  scrapy.Field()
    #LocalTime = scrapy.Field()
    
    # for images
    #image_urls = scrapy.Field()
    #images = scrapy.Field()
    pass
