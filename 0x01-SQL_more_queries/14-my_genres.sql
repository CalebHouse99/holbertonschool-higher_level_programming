-- uses the hbtn_0d_tvshows database to lists all genres
SELECT tv_genres.name, tv_show_genres.genre_id FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name, tv_show_genres.genre_id;
