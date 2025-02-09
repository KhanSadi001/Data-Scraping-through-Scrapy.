import scrapy

class gdpspider(scrapy.Spider): # Change the class name to gdpspider
    name = "gdpspider" # name of spider
    allowed_domains = ["www.worldometers.info"] # allowed domains
    start_urls = ["https://www.worldometers.info/gdp/gdp-by-country/"] # start url

    def parse(self, response): # parse method
        row = response.xpath("//tr") # xpath for the table rows
        for i in row: # loop through the rows
            country = i.xpath("./td/a/text()").get() # xpath for the country name
            gdp = i.xpath("./td[3]/text()").get()   # xpath for the GDP value
            
            yield { # yield the data
                "Country":country, # country name
                "GDP(nominal,2022)":gdp, # GDP value
             }
