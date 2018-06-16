CREATE OR REPLACE VIEW CARS AS
SELECT cars.make, cars.model, cars._condition, cars.source, cars.url, cars.price, cars.year, cars.mileage, cars.photos, cars.stock, cars.vin, cars.dealer, cars.key_features, cars.key_specs, cars.color, research.nhtsa_rating, research.base_features, research.base_specs, research.customer_reviews, research.customer_rating, research.jd_rating 
FROM cars LEFT JOIN research 
ON cars.research_link = research.link;

CREATE OR REPLACE VIEW MODELS AS
SELECT m.make, m.model, m.photo, c._count
FROM models m 
LEFT JOIN (SELECT model, count(model) _count FROM cars GROUP BY model) c 
ON m.model = c.model ORDER BY m.make;
