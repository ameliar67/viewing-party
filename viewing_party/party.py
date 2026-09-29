# ------------- WAVE 1 --------------------

KEY_MOVIE_TITLE = "title"
KEY_MOVIE_GENRE = "genre"
KEY_MOVIE_RATING = "rating"

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        KEY_MOVIE_TITLE: title,
        KEY_MOVIE_GENRE: genre,
        KEY_MOVIE_RATING: rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie[KEY_MOVIE_TITLE] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    total_rating = 0.0

    watched_movies = user_data['watched']
    if not watched_movies:
        return 0.0

    for movie in watched_movies:
        total_rating += movie[KEY_MOVIE_RATING]

    return total_rating / len(user_data['watched'])

def get_most_watched_genre(user_data):

    if len(user_data["watched"]) == 0:
        return None

    genres = {}

    for movie in user_data["watched"]:
        if movie[KEY_MOVIE_GENRE] in genres:
            genres[movie[KEY_MOVIE_GENRE]] += 1
        else:
            genres[movie[KEY_MOVIE_GENRE]] = 1

    current_highest_genre = ''
    current_highest_genre_count = 0

    for genre, count in genres.items():
        if count > current_highest_genre_count:
            current_highest_genre_count = count
            current_highest_genre = genre

    return current_highest_genre 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    movies_friends_havent_watched = []
    titles_friends_have_watched = set()

    for friend in user_data['friends']:
        for movie in friend['watched']:
            titles_friends_have_watched.add(movie[KEY_MOVIE_TITLE])
            
    for movie in user_data['watched']:   
        if movie[KEY_MOVIE_TITLE] not in titles_friends_have_watched:
            movies_friends_havent_watched.append(movie)

    return movies_friends_havent_watched


def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friends_unique_movies_thus_far = set()

    for friend in user_data["friends"]:
        user_watched_set = set()

        for movie in user_data['watched']:
            user_watched_set.add(movie['title'])
        for movie in friend["watched"]:
            if movie['title'] not in user_watched_set and movie['title'] not in friends_unique_movies_thus_far:
                friends_unique_movies.append(movie)
                friends_unique_movies_thus_far.add(movie['title'])

    return friends_unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []

    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:
        if movie['host'] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommendations = []

    if len(user_data["watched"]) == 0:
        return recommendations

    popular_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movie in friends_unique_movies:
        if (movie[KEY_MOVIE_GENRE] == popular_genre
            and movie not in recommendations
        ):
            recommendations.append(movie)

    return recommendations


def get_rec_from_favorites(user_data):
    recommendations = []

    for movie in user_data["favorites"]:
        watched_by_friend = False

        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                watched_by_friend = True
                break

        if not watched_by_friend:
            recommendations.append(movie)

    return recommendations
