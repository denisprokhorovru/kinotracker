from fastapi import FastAPI, HTTPException
from movie_class import Movie, MovieTracker
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="КиноТрекер")

# Разрешаем запросы от фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # разрешить все источники (для разработки)
    allow_methods=["*"],  # разрешить все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # разрешить все заголовки
)


# Создаём трекер и загружаем данные из JSON
tracker = MovieTracker()
tracker.load_from_json("movies.json")


@app.get("/movies")
def get_all_movies():
    """Возвращает список ВСЕХ фильмов."""
    return tracker.get_all_titles()


@app.get("/movies/watched")
def get_watched():
    """Возвращает список просмотренных фильмов."""
    watched = tracker.get_watched_movies()
    return [m.to_dict() for m in watched]


class MovieCreate(BaseModel):
    """Модель для создания нового фильма (валидация)."""
    title: str
    year: int
    genre: str
    rating: float
    seasons: int = 1
    duration: int


@app.get("/movies/{title}")
def find_movie(title: str):
    for mov in tracker.movies:
        if mov.title == title:
            return mov.to_dict()
    raise HTTPException(status_code=404, detail="Фильм не найден")


@app.post("/movies")
def add_movie(movie_data: MovieCreate):
    """Добавляет новый фильм в трекер."""
    new_movie = Movie(
        title=movie_data.title,
        year=movie_data.year,
        genre=movie_data.genre,
        rating=movie_data.rating,
        seasons=movie_data.seasons,
        duration=movie_data.duration
    )
    tracker.add_movie(new_movie)
    tracker.save_to_json("movies.json")
    return {"message": f"Фильм '{movie_data.title}' добавлен!", "movie": new_movie.to_dict()}


@app.put("/movies/{title}/watch")
def mark_watched(title: str):
    """Отмечает фильм просмотренным."""
    for mov in tracker.movies:
        if mov.title == title:
            mov.watch()
            tracker.save_to_json("movies.json")
            return {"message": f"Фильм '{title}' отмечен как просмотренный!"}
    raise HTTPException(status_code=404, detail="Фильм не найден")


@app.delete("/movies/{title}")
def delete_movie(title: str):
    """Удаляет фильм по названию."""
    for mov in tracker.movies:
        if mov.title == title:
            tracker.movies.remove(mov)
            tracker.save_to_json("movies.json")
            return {"message": f"Фильм '{title}' удалён!"}
    raise HTTPException(status_code=404, detail="Фильм не найден")