document.addEventListener("DOMContentLoaded", function() {

    let movieList = document.getElementById("movie-list")
    let addBtn = document.getElementById("add-btn")
    let addForm = document.getElementById("add-form")
    let submitBtn = document.getElementById("submit-btn")
    let cancelBtn = document.getElementById("cancel-btn")

    // ===== Загрузка фильмов при открытии страницы =====
    function loadMovies() {
        movieList.innerHTML = "";
        fetch("http://127.0.0.1:8000/movies")
            .then(response => response.json())
            .then(movies => {
                for (let title of movies) {
                    let newItem = document.createElement("li")
                    newItem.style.marginBottom = "8px"

                    let textSpan = document.createElement("span")
                    textSpan.textContent = title
                    newItem.appendChild(textSpan)

                    // Кнопка "Просмотрено"
                    let watchBtn = document.createElement("button")
                    watchBtn.textContent = "✅"
                    watchBtn.style.marginLeft = "10px"
                    watchBtn.style.cursor = "pointer"
                    watchBtn.addEventListener("click", function() {
                        fetch(`http://127.0.0.1:8000/movies/${title}/watch`, {
                            method: "PUT"
                        })
                        .then(response => response.json())
                        .then(data => {
                            alert(data.message)
                            loadMovies()
                        })
                    })
                    newItem.appendChild(watchBtn)

                    // Кнопка "Удалить"
                    let deleteBtn = document.createElement("button")
                    deleteBtn.textContent = "🗑️"
                    deleteBtn.style.marginLeft = "5px"
                    deleteBtn.style.cursor = "pointer"
                    deleteBtn.addEventListener("click", function() {
                        if (confirm(`Удалить фильм "${title}"?`)) {
                            fetch(`http://127.0.0.1:8000/movies/${title}`, {
                                method: "DELETE"
                            })
                            .then(response => response.json())
                            .then(data => {
                                alert(data.message)
                                loadMovies()
                            })
                        }
                    })
                    newItem.appendChild(deleteBtn)

                    movieList.appendChild(newItem)
                }
            })
    }

    loadMovies()  // загружаем при открытии

    // ===== Показать форму =====
    addBtn.addEventListener("click", function() {
        addForm.style.display = "block"
    })

    // ===== Скрыть форму (отмена) =====
    cancelBtn.addEventListener("click", function() {
        addForm.style.display = "none"
    })

    // ===== Отправить новый фильм =====
    submitBtn.addEventListener("click", function() {
        let newMovie = {
            title: document.getElementById("title-input").value,
            year: parseInt(document.getElementById("year-input").value),
            genre: document.getElementById("genre-input").value,
            rating: parseFloat(document.getElementById("rating-input").value),
            seasons: parseInt(document.getElementById("seasons-input").value),
            duration: parseInt(document.getElementById("duration-input").value)
        }

        fetch("http://127.0.0.1:8000/movies", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newMovie)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message)         // показываем сообщение
            addForm.style.display = "none"  // скрываем форму
            loadMovies()                // обновляем список
        })
    })

})