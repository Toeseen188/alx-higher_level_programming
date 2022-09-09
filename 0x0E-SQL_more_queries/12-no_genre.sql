-- Script that lists all shows contained in hbtn_0d_tvshows
-- without a genre linked.
SELECT ts.title, ts_g.genre_id
FROM tv_shows AS ts
	LEFT JOIN tv_show_genres AS ts_g
	ON ts.id = ts_g.show_id
WHERE ts_g.show_id IS NULL;
