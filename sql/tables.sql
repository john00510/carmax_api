CREATE TABLE IF NOT EXISTS cars (
    id INT NOT NULL AUTO_INCREMENT,
    make VARCHAR(100),
    model VARCHAR(100),
    _condition VARCHAR(50),
    source VARCHAR(100),
    is_scraped TINYINT,
    is_prescraped TINYINT,
    url VARCHAR(255),
    price INT,
    year VARCHAR(50),
    mileage VARCHAR(50),
    research_link VARCHAR(100),
    photos LONGTEXT,
    stock INT,
    vin VARCHAR(100),
    dealer MEDIUMTEXT,
    key_features VARCHAR(255),
    key_specs VARCHAR(255),
    color VARCHAR(100),
    nhtsa_rating VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE KEY url_key (url)
);

CREATE TABLE IF NOT EXISTS research (
    id INT NOT NULL AUTO_INCREMENT,
    make VARCHAR(100),
    model VARCHAR(100),
    year VARCHAR(50),
    base_features LONGTEXT,
    base_specs LONGTEXT,
    customer_reviews LONGTEXT,
    customer_rating VARCHAR(50),
    jd_rating VARCHAR(255),
    link VARCHAR(100),
    PRIMARY KEY (id),
    UNIQUE KEY link_key (link)
);

