from unittest.mock import MagicMock

import pytest

from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="Director 1")
    director_2 = Director(id=2, name="Director 2")
    director_3 = Director(id=3, name="Director 3")

    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.get_one = MagicMock(return_value=director_2)
    director_dao.create = MagicMock(return_value=director_3)
    director_dao.update = MagicMock(return_value=Director(name="New Director"))
    director_dao.delete = MagicMock(return_value=None)

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="Genre 1")
    genre_2 = Genre(id=2, name="Genre 2")
    genre_3 = Genre(id=3, name="Genre 3")

    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.get_one = MagicMock(return_value=genre_2)
    genre_dao.create = MagicMock(return_value=genre_3)
    genre_dao.update = MagicMock(return_value=Genre(name="New Genre"))
    genre_dao.delete = MagicMock(return_value=None)

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(
        id=1, title="title 1", description="Description 1",
        trailer="trailer 1", year=2000, rating=5.9, genre_id=1, director_id=1)
    movie_2 = Movie(
        id=2, title="title 2", description="Description 2",
        trailer="trailer 2", year=2000, rating=5.9, genre_id=2, director_id=2)
    movie_3 = Movie(
        id=3, title="title 3", description="Description 3",
        trailer="trailer 3", year=2000, rating=5.9, genre_id=3, director_id=3)

    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.create = MagicMock(return_value=movie_2)
    movie_dao.update = MagicMock(return_value=Movie(
        title="New Movie", description="New description",
        trailer="new trailer", year=2008, rating=1.0,
        genre_id=3, director_id=3
    ))
    movie_dao.delete = MagicMock(return_value=None)

    return movie_dao
