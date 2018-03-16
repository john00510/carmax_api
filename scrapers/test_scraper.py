from base_scraper import BaseScraper
import time, json

class TestScraper(BaseScraper):
    def __init__(self):
        self.base_url = 'https://www.carmax.com/research/acura/ilx-hybrid/2013'
        BaseScraper.__init__(self)

    def main(self):
        self.get_geckodriver(self.base_url)
        self.get_ratings()
        self.driver.quit()

    def get_ratings(self):
        link = '//a[contains(text(), "See All Ratings")]'
        self.driver.find_element_by_xpath(link).click()
        time.sleep(5)
        elements = '//div[@class="research-page--section"]'
        elements = self.driver.find_elements_by_xpath(elements)
        ##### nhtsa safety rating
        elements1 = './/div[@class="research-page--table-row"]'
        elements1 = elements[0].find_elements_by_xpath(elements1)
        self.nhtsa_rating = {}

        if len(elements1) > 0:
            for row in elements1:
                els = row.find_elements_by_xpath('./div')
                label = els[0].text.strip()
                var1 = els[1].find_element_by_xpath('./span').text.strip()
                try:
                    val1 = els[1].find_element_by_xpath('.//meta[@itemprop="ratingValue"]').get_attribute('content')
                except:
                    val1 = None
                var2 = els[2].find_element_by_xpath('./span').text.strip()
                try:
                    val2 = els[2].find_element_by_xpath('.//meta[@itemprop="ratingValue"]').get_attribute('content')
                except:
                    val2 = None

                self.nhtsa_rating[label]= {var1:  val1, var2: val2}

            self.nhtsa_rating = json.dumps(self.nhtsa_rating)

        ##### jd power reliability rating
        elements2 = './/div[@class="research-page--table-row"]'
        elements2 = elements[1].find_elements_by_xpath(elements2)
        if len(elements2) > 0:
            pass

if __name__ == "__main__":
    TestScraper()
