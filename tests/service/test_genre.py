import pytest

from app.service.genre import GenreService
from ..conftest import genre_dao

class TestDirectorService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(2)

        assert genre is not None
        assert genre.id is not None

    def test_create(self):
        genre_data = {
            "name": "Genre 3",
        }

        genre = self.genre_service.create(genre_data)

        assert genre is not None
        assert genre.id is not None
        assert genre.name == "Genre 3"

    def test_update(self):
        genre_data = {
            "id": 3,
            "name": "New Genre",
        }

        genre = self.genre_service.update(genre_data)

        assert genre.name is not None
        assert genre.name == "New Genre"

    def test_delete(self):
        genre = self.genre_service.delete(3)

        assert genre is None
