from base_scraper import BaseScraper
import time, traceback

class PageScraper(BaseScraper):
    def __init__(self):
        self.counter = 0
        self.base_url = 'https://www.carmax.com/cars/'
        BaseScraper.__init__(self)

    def main(self):
        self.set_is_prescraped()
        self.fh = open(self.base_dir + '/logs/page_scraper.log', 'w')
        self.get_makes()
#        self.delete_sold()
        self.fh.close()

    def get_makes(self):
        elements = '//h2[contains(text(), "Shop by Make")]/following-sibling::ul[@class="list"]/li/a'
        self.get_geckodriver(self.base_url)
        time.sleep(5)
        elements = self.driver.find_elements_by_xpath(elements)
        makes = [element.get_attribute('href') for element in elements]
        self.driver.quit()

        for make in makes:
            self.scrape_make(make)        

    def scrape_make(self, url):
        make = url.split('/')[-1]
        start = time.time()
        self.get_geckodriver(url)

        while True:
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            page_num = self.scrape_page()

            try:
                end = time.time()
                print make, page_num, end - start
                start = time.time()
                self.click_next_page()
            except:
                self.driver.quit()
                break

    def scrape_page(self):
        elements = '//div[@class="vehicle-browse--result"]'
        elements = self.driver.find_elements_by_xpath(elements)

        query = """INSERT INTO cars(source, is_scraped, is_prescraped, make, model,
                stock, vin, _condition, url, price, mileage, year, photos, color,
                key_features, key_specs, dealer, nhtsa_rating, research_link) VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE price = %s, is_prescraped = %s"""
       
        for element in elements:
            try:
                url = self.get_url(element)
                source = self.get_source()
                is_scraped = self.is_scraped()
                is_prescraped = self.is_prescraped()
                make = self.get_make(element)
                model = self.get_model(element)
                stock = self.get_stock(element)
                vin = self.get_vin(element)
                condition = self.get_condition(element)
                price = self.get_price(element)
                mileage = self.get_mileage(element)
                year = self.get_year(element)
                photos = self.get_photos(element)
                key_features = self.get_key_features(element)
                key_specs = self.get_key_specs(element)
                color = self.get_color(key_specs)
                dealer = self.get_dealer(element)
                nhtsa = self.get_nhtsa_frontal_rating(element)
                research_link = self.get_research_link(make, model, year)

                item = (
                    source,
                    is_scraped,
                    is_prescraped,
                    make,
                    model,
                    stock,
                    vin,
                    condition,
                    url,
                    price,
                    mileage,
                    year,
                    photos,
                    color,
                    key_features,
                    key_specs,
                    dealer,
                    nhtsa,
                    research_link,
                    price, 
                    is_prescraped
                )
                self.cur.execute(query, item)
            except:
                error = url + '\n' + traceback.format_exc() + '\n'
                print error
                self.fh.write(error)

        self.conn.commit()
        self.counter += 1
        return self.counter

    def get_source(self):
        return 'carmax.com'

    def get_make(self, _element):
        element = './/meta[@itemprop="brand"]'
        return _element.find_element_by_xpath(element).get_attribute('content')

    def get_model(self, _element):
        element = './/meta[@itemprop="model"]'
        return _element.find_element_by_xpath(element).get_attribute('content')

    def get_vin(self, _element):
        element = './/meta[@itemprop="vehicleIdentificationNumber"]'
        return _element.find_element_by_xpath(element).get_attribute('content')

    def get_condition(self, _element):
        element = './/meta[@itemprop="itemCondition"]'
        return _element.find_element_by_xpath(element).get_attribute('content')

    def get_url(self, _element):
        element = './/h3[@class="vehicle-browse--result-title"]/a'
        return _element.find_element_by_xpath(element).get_attribute('href')

    def is_scraped(self):
        return 0

    def is_prescraped(self):
        return 1

    def get_price(self, _element):
        element = './/div[@class="vehicle-browse--result--info"]'
        element = _element.find_element_by_xpath(element)
        return int(element.get_attribute('data-vehicle-price'))

    def get_year(self, _element):
        element = './/span[@class="vehicle-browse--result-title-description"]'
        element = _element.find_element_by_xpath(element)
        element = element.get_attribute('content')
        return element.split(' ')[1]

    def get_mileage(self, _element):
        element = './/span[@itemprop="mileageFromOdometer"]'
        element = _element.find_element_by_xpath(element).text
        return element
    
    def get_photos(self, _element):
        elements = './/div[contains(@class, "slick-slide")]/a/img'
        elements = _element.find_elements_by_xpath(elements)
        elements = [el.get_attribute('src') for el in elements]
        return ','.join(elements)

    def get_stock(self, _element):
        return int(_element.get_attribute('data-stock-number'))

    def get_dealer(self, _element):
        element = './/div[contains(@class, "result--blurb-location")]/div'
        element = _element.find_element_by_xpath(element)
        return element.text

    def get_key_features(self, _element):
        element = './/span[@itemprop="vehicleConfiguration"]'
        element = _element.find_elements_by_xpath(element)[0]
        return element.get_attribute('innerHTML')

    def get_key_specs(self, _element):
        element = './/span[@itemprop="vehicleConfiguration"]'
        element = _element.find_elements_by_xpath(element)[1]
        return element.get_attribute('innerHTML')

    def get_color(self, element):
        return element.split(' ')[-1].split('/')[0]

    def get_nhtsa_frontal_rating(self, _element):
        element = './/a[contains(text(), "NHTSA")]'
        element = _element.find_element_by_xpath(element)
        return element.get_attribute('href')

    def set_is_prescraped(self):
        query = """UPDATE cars SET is_prescraped = 0"""
        self.cur.execute(query)
        self.conn.commit()

    def delete_sold(self):
        query = """DELETE FROM cars where is_prescraped = 0"""
        self.cur.execute(query)
        self.conn.commit()

    def click_next_page(self):
        element = '//a[@class="pagination--next"]'
        self.wait_visibility(self.driver, element, 30).click()

if __name__ == "__main__":
    PageScraper()

