# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

