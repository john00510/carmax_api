from base_scraper import BaseScraper
import time, traceback

class ResearchScraper(BaseScraper):
    def __init__(self):
        self.count = 0
        self.base_url = 'https://carmax.com/research/'
        BaseScraper.__init__(self)

    def main(self):
        self.fh = open(self.base_dir + '/logs/research_scraper.log', 'w')
        self.get_geckodriver(self.base_url)
        makes = self.get_makes()
        self.driver.quit()

        for make in makes:
            self.get_models(make)

    def get_makes(self):
        elements = '//a[@class="link-plantation--item-search-all-link"]'
        elements = self.driver.find_elements_by_xpath(elements)
        return [element.get_attribute('href') for element in elements]

    def get_models(self, url):
        elements = '//a[@class="tile--item--row"]'
        self.get_geckodriver(url)
        time.sleep(5)
        elements = self.driver.find_elements_by_xpath(elements)
        models = [element.get_attribute('href') for element in elements]        
        self.driver.quit()

        for model in models:
            self.get_years(model)

    def get_years(self, url):
        elements = '//a[@class="make-model-year-tile--research-link"]'
        self.get_geckodriver(url)
        time.sleep(5)
        elements = self.driver.find_elements_by_xpath(elements)
        years = [element.get_attribute('href') for element in elements]
        self.driver.quit()

        for year in years:
            self.scrape_page(year)

    def scrape_page(self, url):
# https://www.carmax.com/research/acura/ilx/2016
        query = """ INSERT IGNORE INTO research(make, model, year, base_features, 
            base_specs, reviews, jd_rating, link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        self.get_geckodriver(url)
        time.sleep(5)

        if self.get_status_code() != '404 Error':
            make = self.get_make(url)
            model = self.get_model(url)
            year = self.get_year(url)
            link = self.get_research_link(make, model, year)
            print link
            #base_specs = self.get_base_specs()
            #base_features = self.get_base_features()
            #jd_rating = self.get_jd_rating()
            #reviews = self.get_reviews()
            self.count += 1

        self.driver.quit()

    def get_make(self, url):
        return url.split('/')[-3]

    def get_model(self, url):
        return url.split('/')[-2]

    def get_year(self, url):
        return url.split('/')[-1]

    def get_base_features(self):
        return ''

    def get_base_specs(self):
        return ''

    def get_jd_rating(self):
        elements = '//div[@class="reliability-ratings-card--row"]/div'
        elements = self.driver.find_elements_by_xpath(elements)

#        for element in elements:
#            _elements = element.find_elements_by_xpath('./div')
        print len(elements)

    def get_reviews(self):
        return ''

if __name__ == "__main__":
    ResearchScraper()

