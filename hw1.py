# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    #
    movie_dictionary = {}  # Create an empty dictionary to store movie ratings

    with open(f, 'r') as content:  # Use the parameter f for flexibility
        for line in content:
            movie, rating_str, _ = line.strip().split('|')
            rating = float(rating_str)  # Convert rating from string to float
            if movie in movie_dictionary:
                movie_dictionary[movie].append(rating)  # Append the float rating to the existing list
            else:
                movie_dictionary[movie] = [rating]  # Create a new list with the float rating

    return movie_dictionary
# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    genre_dictionary = {}
    with open(f, 'r') as content:
        for line in content:
            genre, _, movie = line.strip().split('|')  # Split each line and ignore the ID
            genre_dictionary[movie] = genre  # Map movie to genre in the dictionary
    return genre_dictionary

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    movies_to_genre = {}  # Initialize an empty dictionary to store genres as keys and list of movies as values.

    for movie, genre in d.items():
        if genre not in movies_to_genre:
            movies_to_genre[genre] = [movie]  # Create a new list for this genre with the movie.
        else:
            movies_to_genre[genre].append(movie)  # Append the movie to the existing list for this genre.

    return movies_to_genre
    
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    average_rating_dict = {}  # Initialize an empty dictionary to store the average ratings

    for movie, ratings in d.items():
        if isinstance(ratings, list):  # Check if ratings is a list
            average_rating = sum(ratings) / len(ratings)

              # Calculate the average rating
        else:
            average_rating = ratings  # If it's a single rating, use it directly
        average_rating_dict[movie] = average_rating  # Add the average rating to the dictionary

    return average_rating_dict
    
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    sorted_movies = sorted(d.items(), key=lambda item: item[1], reverse=True)[:n]
    # Convert the sorted list of tuples back to a dictionary
    popular_movies = {movie: rating for movie, rating in sorted_movies}
    
    return popular_movies

    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    filtered_movies = {movie: rating for movie, rating in d.items() if rating >= thres_rating}
    return filtered_movies
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    popular_in_genre = []
    movies = genre_to_movies[genre]
    
    for movie, rating in movie_to_average_rating.items():
        if movie in movies:
            popular_in_genre.append((movie, rating))
    popular_in_genre = sorted(popular_in_genre, key = lambda x:x[1], reverse=True)
    
    return dict(popular_in_genre[:n])
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    ratings = []
    movies = genre_to_movies.get(genre, [])
        
    for movie in movies:
        if movie in movie_to_average_rating:
            ratings.append(movie_to_average_rating[movie])
        
    if len(ratings) > 0:
        genre_rating = sum(ratings) / len(ratings)
        return genre_rating
    else:
        return 0
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    gen_popularity = [
    (genre, get_genre_rating(genre, genre_to_movies, movie_to_average_rating))
    for genre in genre_to_movies
    ]

    # Sort genres by their average rating in descending order and select the top n
    gen_popularity = sorted(gen_popularity, key=lambda x: x[1], reverse=True)[:n]

    # Convert the sorted list of tuples to a dictionary
    return dict(gen_popularity)

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    user_ratings = {}

    with open(f, 'r') as file:
        for line in file:
            # Assuming the file format is "movie|rating|user_id"
            movie, rating_str, user_id_str = line.strip().split('|')
            # Convert the rating to float and user_id to int
            rating = float(rating_str)
            user_id = int(user_id_str)
            # Create a tuple for the movie and its rating
            movie_name_ratings = (movie, rating)
            
            # Check if the user_id exists in the dictionary
            if user_id in user_ratings:
                user_ratings[user_id].append(movie_name_ratings)
            else:
                user_ratings[user_id] = [movie_name_ratings]
                
    return user_ratings
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    genre_count = defaultdict(int)
    for movie, _ in user_to_movies.get(user_id, []):
        genre = movie_to_genre.get(movie)
        if genre:
            genre_count[genre] += 1

    if not genre_count:
        return None  # or "No favorite genre" if no movies have been rated

    return max(genre_count, key=genre_count.get)

    
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    favorite_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    if not favorite_genre:
        return {}  # No recommendations if no favorite genre

    # Filter movies that the user has not rated and are in their favorite genre
    user_rated_movies = {movie for movie, _ in user_to_movies.get(user_id, [])}
    recommended_movies = {
        movie: rating for movie, rating in movie_to_average_rating.items()
        if movie not in user_rated_movies and movie_to_genre.get(movie) == favorite_genre
    }

    # Sort the recommended movies by their average rating in descending order
    recommended_movies = dict(sorted(recommended_movies.items(), key=lambda item: item[1], reverse=True))

    return recommended_movies
    

# -------- main function for your testing -----
def main():
    """
    # write all your test code here
    # this function will be ignored by us when grading
    
    #Test 1
    movie_dict = read_ratings_data("movieRatingSample.txt")
    #print(movie_dict)
    
    #Test 2
    genre_dict = read_movie_genre("movieGenreSample.txt")
   #print(genre_dict) 
    
    #Test 3

    genre_to_movies_dict = create_genre_dict(genre_dict)
    #print(genre_to_movies_dict)
    

    #Test 4    
    average_ratings = calculate_average_rating(movie_dict)
    #print(average_ratings)
    
    #Test 5
    popular_movies = get_popular_movies(average_ratings)
    #print(popular_movies)

    #Test 6
    filtered_movies = filter_movies(average_ratings)
    #print(filtered_movies)

    #Test 7
    users = read_user_ratings("movieRatingSample.txt")
    #print(users)
    """
    a1 = read_ratings_data("movieRatingSample.txt")
    a2 = read_movie_genre("movieGenreSample.txt")
    print("1.1")
    print(a1)
    print("\n1.2")
    print(a2)

    b1 = create_genre_dict(a2)
    b2 = calculate_average_rating(a1)

    print("\n2.1")
    print(b1)
    print("\n2.2")
    print(b2)

    c1 = get_popular_movies(b2)
    c2 = filter_movies(b2)
    c3 = get_popular_in_genre("Action", b1, b2)
    c4 = get_genre_rating("Action", b1, b2)
    c5 = genre_popularity(b1, b2)
    print("\n3.1")
    print(c1)
    print("\n3.2")
    print(c2)
    print("\n3.3")
    print(c3)
    print("\n3.4")
    print(c4)
    print("\n3.5")
    print(c5)

    d1 = read_user_ratings("movieRatingSample.txt")
    d2 = get_user_genre(6, d1, a2)
    d3 = recommend_movies(1, d1, a2, b2)
    print("\n4.1")
    print(d1)
    print("\n4.2")
    print(d2)
    print("\n4.3")
    print(d3)





    

    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()

    
