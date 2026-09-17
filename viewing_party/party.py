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

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
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


def get_friends_unique_watched(user_data):
    friends_unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)

    return friends_unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (
                movie not in user_data["watched"]
                and movie["host"] in user_data["subscriptions"]
                and movie not in recommendations
            ):
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

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (
                movie not in user_data["watched"]
                and movie["genre"] == popular_genre
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
