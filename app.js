// Ждём, пока страница полностью загрузится
document.addEventListener("DOMContentLoaded", function() {

    // Находим список на странице
    let movieList = document.getElementById("movie-list")

    // Стучимся к нашему API
    fetch("http://127.0.0.1:8000/movies")
        .then(response => response.json())
        .then(movies => {
            // Для каждого фильма создаём пункт списка
            for (let title of movies) {
                let newItem = document.createElement("li")
                newItem.textContent = title
                movieList.appendChild(newItem)
            }
        })
})