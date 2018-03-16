CREATE OR REPLACE VIEW CARS AS
SELECT cars.make, cars.model, cars._condition, cars.source, cars.url, cars.price, cars.year, cars.mileage, cars.photos, cars.stock, cars.vin, cars.dealer, cars.key_features, cars.key_specs, cars.color, cars.nhtsa_rating, research.base_features, research.base_specs, research.customer_reviews, research.customer_rating, research.jd_rating 
FROM cars LEFT JOIN research 
ON cars.research_link = research.link;

