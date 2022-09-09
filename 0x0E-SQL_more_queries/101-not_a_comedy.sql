-- script that lists all shows without the genre
-- Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
	LEFT JOIN(
		SELECT tv_shows.id, tv_shows.title
		FROM tv_shows
			JOIN tv_show_genres
				ON tv_shows.id = tv_show_genres.show_id
			JOIN tv_genres
				ON tv_genres.id = tv_show_genres.genre_id
		WHERE tv_genres.name = "Comedy"
		ORDER BY tv_shows.id
		) AS comedy_shows
			ON comedy_shows.id = tv_shows.id
WHERE comedy_shows.id IS NULL
ORDER BY tv_shows.title;
