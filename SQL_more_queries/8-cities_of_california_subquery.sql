-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT cities.name

-- Selecting the name of the cities
FROM cities

-- Filtering cities by the state_id that matches California's id
WHERE cities.state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
)

-- Ordering the results by city id in ascending order
ORDER BY cities.id ASC;
