# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import html
from html.parser import HTMLParser
from x500.items import X500Item

class X500Spider(scrapy.Spider):
    name = "x500"
    allowed_domains = ["directory.app.alcatel-lucent.com"]
    start_upi = (
        #'BQ0079905',        
        #'HJ0000334',      #Ye Jianfeng  
        #'CV0004440',     #JI Lijun
        #'HJ0001123',
        'ZZ0052296',      ###Zhang QI
    )
    start_urls = (
        'http://directory.app.alcatel-lucent.com/en/Rupi=%s' % u for u in start_upi
    )
    
    def parse(self, response):
        p = X500Item()

        #His/her own name in English
        #print(response.xpath('//h2[@class="person_title"]/text()'))
        p[u'Ename'] = response.xpath('//h2[@class="person_title"]/text()').extract()[0]
        upi = response.url.split('=')[1]    
        #p['image_urls'] = response.xpath('//div[@class="wrap3"]/img/@src').extract()

        #information except for the supervisor and administrative approver
        #fields = response.xpath('//div[@class="person_item"] | //div[@class="person_item person_h_separator"]')
        fields = response.xpath('//div[@class="person_item"]')
        for f in fields:
            pair = f.xpath('.//div').extract()
            try:
                #pname = re.sub('[ |:|\r|\n]', '', re.sub('<[^>]*>', '', pair[0]))
                pname = ''.join(html.fromstring(pair[0]).xpath('//text()')).replace(':','').strip().replace(' ','')#.encode('utf8')
                #pvalue = html.fromstring(pair[1]).xpath('//div[@class="person_attr_value"]/text()')
                pvalue = ''.join(html.fromstring(pair[1]).xpath('//text()')).strip()#.encode('utf8')
                self.logger.info('name = %s\nvalue= %s' % (pname, pvalue))
                #print('pvalue after xpath = %s' % html.fromstring(pair[1]).xpath('//div[@class="person_attr_value"]/text()').replace('\r\n', ' ').replace('\n', ' ')[0].strip())
                #pvalue = HTMLParser.HTMLParser().unescape(pair[1]).replace('<br>', ' ')     #.encode('utf8')
                #pvalue = re.sub('<[^>]*>', '', pvalue).replace('\r\n', ' ').replace('\n', ' ').strip()
                if pname != u'LocalTime':
                    p[pname] = pvalue
            except Exception as e:
                print(u'####UPI: %s handling error on: %s!' % (upi, pname))
                print(e)
        #his/her sub-decessors
        p[u'Members'] = u';'.join(response.xpath('//li[@class="tree"]/a/text() | //li[@class="last_tree"]/a/text()').extract())
        yield p

        if not self.settings.getbool('DEBUG_MODE'):
            links = response.xpath('//li[@class="tree"]/a/@href | //li[@class="last_tree"]/a/@href').extract()
            for link in links:
                yield scrapy.Request(response.urljoin(link), self.parse)
        pass
