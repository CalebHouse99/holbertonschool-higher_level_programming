-- lists all genres from hbtn_0d_tvshows
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres, tv_show_genres
WHERE tv_show_genres.genre_id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY tv_show_genres.genre_id DESC;
