import pytest

from app.service.movie import MovieService

from ..conftest import movie_dao


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(2)

        assert movie is not None
        assert movie.id is not None

    def test_create(self):
        movie_data = {
            "title": "title 2",
            "description": "Description 2",
            "trailer": "trailer 2",
            "year": 2000,
            "rating": 5.9,
            "genre_id": 2,
            "director_id": 2,
        }

        movie = self.movie_service.create(movie_data)

        assert movie is not None
        assert movie.id is not None
        assert movie.title == "title 2"
        assert movie.description == "Description 2"
        assert movie.trailer == "trailer 2"
        assert movie.year == 2000
        assert movie.rating == 5.9
        assert movie.genre_id == 2
        assert movie.director_id == 2

    def test_update(self):
        movie_data = {
            "id": 1,
            "title": "New Movie",
            "description": "New description",
            "trailer": "new trailer",
            "year": 2008,
            "rating": 1.0,
            "genre_id": 3,
            "director_id": 3,
        }

        movie = self.movie_service.update(movie_data)

        assert movie.title is not None
        assert movie.title == "New Movie"
        assert movie.description == "New description"
        assert movie.trailer == "new trailer"
        assert movie.year == 2008
        assert movie.rating == 1.0

    def test_delete(self):
        movie = self.movie_service.delete(1)

        assert movie is None
