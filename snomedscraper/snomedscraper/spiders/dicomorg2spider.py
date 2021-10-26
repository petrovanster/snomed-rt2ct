import scrapy


class Dicomorg2spiderSpider(scrapy.Spider):
    download_timeout = 360
    name = 'dicomorg2spider'
    allowed_domains = ['http://dicom.nema.org']
    start_urls = ['http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_O.html#table_O-1']

    def parse(self, response):
        for row in response.xpath("//div[@class='table']//tbody/tr"):
            data = {
                "SCT": "".join(row.xpath("td[1]//text()").getall()).strip(),
                "SRT": "".join(row.xpath("td[2]//text()").getall()).strip(),
                "SNOMED Fully Specified Name": "".join(row.xpath("td[3]//text()").getall()).strip()
            }
            yield data
        pass
