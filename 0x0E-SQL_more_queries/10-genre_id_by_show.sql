-- Import database dump from bhtn_0d)tvshows to MYSQL server
-- Lists all shows contained in hbtn_)d_tvshows that has at aleast one genre linked
SELECT s.title, g.genre_id
	FROM tv_shows AS s
		INNER JOIN tv_show_genres AS g
		ON s.id = g.shows_id
	ORDER BY s.title, g.genre_id;
