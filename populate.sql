SELECT * FROM genres

SELECT * FROM film
 
SELECT * FROM filmgenres

SELECT * FROM filmrating

SELECT * FROM filmawards

--SELECT * FROM awards
--SELECT * FROM rating_platforms


INSERT INTO
Rating_platforms(platform_id, platform_name)
VALUES
('Metascore', 'Metascore'),
('IMDb', 'Internet Movie Database'),
('Metacritic', 'Metacritic'),
('IGN', 'IGN'),
('Rotten Tomatoes', 'Rotten Tomatoes');

INSERT INTO
Awards(award_id, award_name)
VALUES
('Oscar', 'Oscar'),
('BAFTA', ' BAFTA Film Award'),
('Golden Globe', 'Golden Globe'),
('Saturn', 'Saturn Award'),
('ASC', 'ASC Award');