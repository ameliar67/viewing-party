# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    total_rating = 0.0

    watched_movies = user_data['watched']
    if len(watched_movies) == 0:
        return 0.0

    for movie in watched_movies:
        total_rating+=movie["rating"]

    return total_rating / len(user_data['watched'])

def get_most_watched_genre(user_data):

    genres = {}
    current_highest_genre = ''
    current_highest_genre_count = 0

    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        if movie['genre'] in genres:
            genres[movie['genre']]+=1
        else:
            genres[movie['genre']] = 1

    for genre in genres.keys():
        if genres[genre] > current_highest_genre_count:
            current_highest_genre_count = genres[genre]
            current_highest_genre = genre

    return current_highest_genre 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    movies_friends_havent_watched = []
    titles_friends_have_watched = {}

    for friend in user_data['friends']:
        for movie in friend['watched']:
            titles_friends_have_watched[movie['title']] = 1
            
    for movie in user_data['watched']:   
        if movie['title'] not in titles_friends_have_watched:
            movies_friends_havent_watched.append(movie)

    return movies_friends_havent_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

