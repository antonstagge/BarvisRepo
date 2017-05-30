#Defines the tables used in the database for Barvis, your automated home system.
#
#Created by Fredrik Omstedt, Cristian Osorio Bretti and Anton Stagge

#Defines lists that Barvis can store, containing different list elements.
CREATE TABLE list (
    list_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

#Defines list elements that are contained within lists.
CREATE TABLE list_element (
    list_element_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    list INT UNSIGNED NOT NULL REFERENCES list(list_id) ON UPDATE CASCADE ON DELETE CASCADE
);