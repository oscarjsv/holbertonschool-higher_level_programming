-- comentario
SELECT tv_genres.name
FROM tv_shows
RIGHT JOIN tv_genres
ON tv_shows.id = tv_genres.id
WHERE title = 'Dexter' and tv_genres.id is NOT NULL
ORDER BY
tv_genres.name ASC;
