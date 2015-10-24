import scrapy

class MySpider(scrapy.Spider):
	name = "tripadvisor.com"
	allowed_domains = "tripadvisor.com"
	start_urls = [
		'http://www.tripadvisor.com/Restaurants-g187457-San_Sebastian_Donostia_Guipuzcoa_Province_Basque_Country.html'
	]	

	def parse (self, response):
		print("callback...............")
		#restaurant = response.xpath()(
		#	'//h3[@class="title"]/a//@href').extract()

		next_url = response.xpath('//a[text()="Next"]/@href').extract()
		next_url = response.urljoin(next_url[0])
		print("NEXT URL = "+ str(next_url))
		yield scrapy.Request(next_url, callback = self.parse)
		


