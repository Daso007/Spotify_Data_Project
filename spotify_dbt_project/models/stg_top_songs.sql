-- This is our first dbt model!
-- It selects from our raw data source and adds a new column.

select
    track_id,
    track_name,
    artist_name,
    album_name,
    popularity,
    case
        when popularity >= 80 then 'Global Hit'
        when popularity >=60 and popularity < 80 then 'Popular'
        Else 'Niche' 
    End as popular_category

from
    {{ source('spotify_raw_data', 'top_songs') }}