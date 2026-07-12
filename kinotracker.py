# Структура фильма:
# {"title": str, "year": int, "genre": str, "rating": float,"is_watched": bool, "seasons": int, "duration": int}
# seasons = 1 для фильмов, > 1 для сериалов

import json


def load_movies(filename):
    """Читает список фильмов из JSON-файла"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

movies = load_movies("movies.json")


def average_rating(movies_list):
    """Вычисляет средний рейтинг всех фильмов в списке.
    Принимает:
        movies_list (list): список словарей с ключом "rating"
    Возвращает:
        float: среднее арифметическое всех рейтингов
    """

    total = 0
    for movie in movies_list:
        total += movie["rating"]
    return total / len(movies_list)

print()
print(f"Рейтинг всех фильмов = {average_rating(movies)}")
print()


def get_all_titles(movies_list):
    """Достаём название всех фильмов
    Принимает: список фильмов
    Возвращает: список только с названиями фильмов
    """

    title_list = []
    for name in movies_list:
        title_list.append(name["title"])
    return title_list

print(get_all_titles(movies))
print()


def get_watched_movies(movies_list):
    """Достаём из списка фильмов только те, которые были просмотрены
    Принимает:
        Список с фильмами
    Возвращает:
        Список фильмов которые уже смотрел, со всей информацией о нём"""
    
    watched_list = []
    for movie in movies_list:
        if movie["is_watched"] == True:
            watched_list.append(movie)
    return watched_list

print(get_watched_movies(movies))
print()


def save_movies(filename, movies_list):
    """Сохраняет список фильмов в JSON-файл"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(movies_list, file, ensure_ascii=False, indent=4)


def add_movie(filename, movies_list, title, year, genre, rating, is_watched, seasons, duration):
    """Добавляет новый фильм.
    Принимает:
        Название, год, основной жанр, рейтинг, смотрел ли, количество серий, время серии
    Далее добавляет в наш список movies этот фильм.
    """

    new_movie = {"title": title, "year": year, "genre": genre, "rating": rating, "is_watched": is_watched, "seasons": seasons, "duration": duration}
    movies_list.append(new_movie)
    save_movies(filename, movies_list)


add_movie("movies.json", movies, "Горничная", 2025, "драма", 5, False, 1, 131)
print(movies)
print()