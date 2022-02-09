CREATE TABLE album(
	id SERIAL PRIMARY KEY,
	title VARCHAR(128),
	artist_id INTEGER REFERENCES artist(id) ON DELETE CASCADE
);

CREATE TABLE track(
	id SERIAL PRIMARY KEY,
	title VARCHAR(128),
	len INTEGER,
	rating INTEGER,
	COUNT INTEGER,
	artist_id INTEGER REFERENCES album(id) ON DELETE CASCADE,
	genre_id INTEGER REFERENCES genre(id) ON DELETE CASCADE,
);


INSERT INTO genre(id,name) VALUES(1,'Rock');
INSERT INTO genre(id,name) VALUES(2,'Metal');

INSERT INTO artist(id,name) VALUES(1,'Led Zeppelin');
INSERT INTO artist(id,name) VALUES(2,'AC/DC');

INSERT INTO album (id,title, artist_id) VALUES(1,'Who made who', 2);
INSERT INTO album (id,title, artist_id) VALUES(2,'IV', 1);



INSERT INTO track(title, rating, len, COUNT, album_id, genre_id)
   VALUES  ('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO track(title, rating, len, COUNT, album_id, genre_id)
   VALUES  ('Stairway', 5, 482, 0, 2, 1);

INSERT INTO track(title, rating, len, COUNT, album_id, genre_id)
   VALUES  ('About to Rock', 5, 313, 0, 1, 2);
INSERT INTO track(title, rating, len, COUNT, album_id, genre_id)
   VALUES  ('Who Made Who', 5, 207, 0, 1, 2);


SELECT album.title, artist.name FROM album JOIN artist ON album.artist_id = artist.id;
