-- script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name,

-- Subquery to get the state name for each city
(SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name

FROM cities

-- Ordering the results by city id in ascending order
ORDER BY cities.id ASC;
