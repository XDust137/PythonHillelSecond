import scrapy


class WorkUaSpider(scrapy.Spider):
    name = 'work_ua'
    allowed_domains = ['work.ua']
    start_urls = ['https://www.work.ua/resumes-python/']

    def parse(self, response):

        for item in response.css('div.card.resume-link'):

            result = {
                "proposition": item.css('h2 a::text').get(),
                "name": item.css('div b::text').get(),
                "age": item.css('div span:nth-child(3)::text').get(),
                "city": item.css('div span:nth-child(5)::text').get(),
            }

            salary = item.css('h2 span span::text').get()
            if salary:
                result['salary'] = int(salary.split()[0])

            yield result

        for i in response.css('#pjax-resume-list nav li'):
            if i.css('a::text').get() == 'Наступна':
                yield response.follow(url=i.css('a::attr(href)').get(), callback=self.parse)


