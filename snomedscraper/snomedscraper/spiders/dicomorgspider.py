import scrapy
from scrapy.http import request


class DicomorgspiderSpider(scrapy.Spider):
    name = 'dicomorgspider'
    allowed_domains = ['dicom.nema.org']
    start_urls = ['http://dicom.nema.org/medical/dicom/current/output/chtml/part16/PS3.16.html']

    def parse(self, response):
        cids = response.xpath("//a[contains(text(), 'CID')]")
        for cid in cids:
            yield response.follow(cid, callback=self.parse_cid) # scrapy.Request(cid.attrib['href'], self.parse_cid) 
        pass

    def parse_cid(self, response):
        all = response.xpath("//tbody/tr")
        title = response.xpath("//head/title/text()").get()
        cidnumber = response.xpath("//head/title/text()").re('CID (\d+)')
        for line in all:
            data =  {
                "CID": title, 
                "CID number": cidnumber,
                "Coding Scheme Designator": "".join(line.xpath('td[1]//text()').getall()).strip(),
                "Code Value": "".join(line.xpath('td[2]//text()').getall()).strip(),
                "Code Meaning": "".join(line.xpath('td[3]//text()').getall()).strip(),
                "SNOMED-RT ID": "".join(line.xpath('td[4]//text()').getall()).strip(),
                "SNOMED URL": "".join(line.xpath('td[4]/p/a[@class="link"]/@href').getall()).strip()
            }
            yield data
            pass
        pass
