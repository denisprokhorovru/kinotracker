import json


class Movie:
    """Класс, представляющий фильм или сериал."""
    
    def __init__(self, title, year, genre, rating, seasons, duration):
        """Инициализация нового объекта Movie."""
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating
        self.is_watched = False
        self.seasons = seasons
        self.duration = duration
    
    def watch(self):
        """Отметить фильм как просмотренный."""
        self.is_watched = True

    def to_dict(self):
        """Возвращает словарь с данными фильма (для JSON)."""
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "rating": self.rating,
            "is_watched": self.is_watched,
            "seasons": self.seasons,
            "duration": self.duration
        }


class MovieTracker:
    """Класс для управления коллекцией фильмов."""
    
    def __init__(self):
        """Инициализация пустого списка фильмов."""
        self.movies = []  # список объектов Movie

    def add_movie(self, movie):
        """Добавляет объект Movie в список."""
        self.movies.append(movie)

    def get_watched_movies(self):
        watched_list = []
        for movie in self.movies:
            if movie.is_watched == True:
                watched_list.append(movie)
        return watched_list
    
    def get_all_titles(self):
        """Возвращает список названий всех фильмов."""
        titles = []
        for movie in self.movies:
            titles.append(movie.title)
        return titles
    
    def save_to_json(self, filename):
        """Сохраняет список фильмов в JSON-файл."""
        movies_dicts = []
        for movie in self.movies:
            movies_dicts.append(movie.to_dict())
        
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(movies_dicts, file, ensure_ascii=False, indent=4)
    
    def load_from_json(self, filename):
        """Загружает фильмы из JSON-файла в трекер."""
        with open(filename, "r", encoding="utf-8") as file:
            movies_dicts = json.load(file)
        
        self.movies = []  # очищаем текущий список
        for movie_dict in movies_dicts:
            movie = Movie(
                title=movie_dict["title"],
                year=movie_dict["year"],
                genre=movie_dict["genre"],
                rating=movie_dict["rating"],
                seasons=movie_dict["seasons"],
                duration=movie_dict["duration"]
            )
            movie.is_watched = movie_dict["is_watched"]
            self.movies.append(movie)



# Создаём два фильма
dune = Movie("Дюна", 2021, "фантастика", 8.9, 1, 155)
interstellar = Movie("Интерстеллар", 2014, "фантастика", 8.6, 1, 169)

# Проверяем статус до просмотра
print(f"Дюна просмотрена? {dune.is_watched}")
print(f"Интерстеллар просмотрен? {interstellar.is_watched}")

# Отмечаем Дюну как просмотренную
dune.watch()

# Проверяем после
print(f"Дюна просмотрена? {dune.is_watched}")
print(f"Интерстеллар просмотрен? {interstellar.is_watched}")
tracker = MovieTracker()
tracker.add_movie(dune)
tracker.add_movie(interstellar)
print(f"Фильмов в трекере: {len(tracker.movies)}")
print(f"Первый фильм: {tracker.movies[0].title}")
watched = tracker.get_watched_movies()
print(f"Просмотрено фильмов: {len(watched)}")
for m in watched:
    print(f"  - {m.title}")

print(dune.to_dict())
print(tracker.get_all_titles())
tracker.save_to_json("movies.json")
print("Сохранено в movies.json")