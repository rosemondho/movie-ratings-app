from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    new_movie = Movie(title=title, 
                    overview=overview, 
                    release_date=release_date, 
                    poster_path=poster_path)

    db.session.add(new_movie)
    db.session.commit()

    return new_movie


def create_rating(user,movie,score):
    """Create and return the score from the rating"""
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating




if __name__ == '__main__':
    from server import app
    connect_to_db(app)