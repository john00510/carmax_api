from base_scraper import BaseScraper

class CarScraper(BaseScraper):
    def __init__(self):
        BaseScraper.__init__(self)

    def main(self):
        pass

    #Make
    #Model
    def is_scraped(self):
        pass

    def is_prescraped(self):
        pass

    def get_trim_info(self, el):
        pass
    def get_price(self, el):
        pass

    def get_year(self, el):
        pass

    def get_mileage(self, el):
        pass

    def get_reviews(self, el):
        #Customer Reviews (at the vehicle model level, if vehicle model has them)
        pass
    
    def get_photos(self, el):
        pass

    def get_stock(self, el):
        pass

    def get_vin(self, el):
        pass ?

    def get_dealer(self, el):
        #(phone number and location)
        pass

    def get_key_features(self, el):
        pass

    def get_key_specs(self, el):
        #(if any)
        pass

    def get_color(self, el):
        pass

    def get_base_specs(self, el):
        #Vehicle Base specifications (grab all specifications)
        pass

    def get_nhtsa_frontal_rating(self, el):
        #NHTSA Driver Frontal Rating
        pass

    def get_jd_power_rating(self, el):
        #J.D. Power Ratings
        pass

