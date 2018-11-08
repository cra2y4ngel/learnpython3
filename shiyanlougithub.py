import scrapy

class Shiyanlougithub(scrapy.Spider):
	name = 'shiyanlou-github-spider'

	def start_requests(self):
		urllist = ['https://github.com/shiyanlou?before=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wNlQxNzozNjoxNSswODowMM4FkpW2&tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoxOTo1N1rOBZKWMA%3D%3D&tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNVQxMTozMTowNyswODowMM4Bxrsx&tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMFQxMzowMzo1MiswODowMM4BjkvL&tab=repositories']
		urls = (url for url in urllist)
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self,response):
		for subject in response.xpath('//li[@itemprop="owns"]'):
			yield {
			'name':subject.css('a::text').re_first('\n      (.+)'),
			'update_time':subject.css('relative-time::attr(datetime)').extract_first(default='None')
			}