const BASE_URL = "http://0.0.0.0:8000";

function getCookieValue (name) {
  return document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
}

function checkIfLoggedIn(token) {
  msg = document.getElementById("logged-in-message");
  baseMessage = "Logged in as: ";
  fetch(`${BASE_URL}/users/me`, {
    method: "GET",
    headers: new Headers({
      Authorization: "Bearer" + " " + token,
    }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      }
    })
    .then((data) => {
      if (data.username) {
        msg.textContent = baseMessage + data.username;
      } else {
        msg.textContent = "Not logged in";
      }
    })
    .catch((error) => console.log(error));
}

function getToken() {
  document.cookie = "token=;"
  const loginData = document.getElementById("login-form");
  const data = fetch(`${BASE_URL}/token`, {
    method: "POST",
    body: new FormData(loginData),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      document.cookie = "token=" + data.access_token + ";samesite=strict";
      checkIfLoggedIn(data.access_token)
    })
    .catch(function (error) {
      console.log(error);
    });
  loginData.reset();
  document.getElementById("movie-list").textContent = "";
}

function getMovies() {
  token = getCookieValue("token");
  fetch(`${BASE_URL}/users/movie`, {
    method: "GET",
    headers: new Headers({
      Authorization: "Bearer" + " " + token,
    }),
  })
    .then((response) => response.json())
    .then(function (data) {
      var movie_list = document.getElementById("movie-list");
      movie_list.innerHTML = "";
      data.forEach(function (item) {
        var entry = document.createElement("li");
        entry.appendChild(
          document.createTextNode(item.title + " " + item.rating)
        );
        movie_list.appendChild(entry);
      });
    })
    .catch((error) => console.log("error"));
}

function getPublicData() {
  fetch(`${BASE_URL}/public`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then(
      (data) =>
        (document.getElementById("public-data").textContent =
          "From FastAPI: current time is: " + data.current_time)
    )
    .catch((error) => console.log(error));
}

function activateSubmit() {
  button = document.getElementById("submit-movie");
  if (document.getElementById("movie-title").value.length > 0) {
    button.disabled = false;
  } else {
    button.disabled = true;
  }
}
function addMovie() {
  token = getCookieValue("token");
  title = document.getElementById("movie-title");
  rating = document.getElementById("movie-rating");
  fetch(`${BASE_URL}/users/movie`, {
    method: "POST",
    headers: new Headers({
      Authorization: "Bearer" + " " + token,
    }),
    body: JSON.stringify({
      title: title.value,
      rating: rating.value,
    }),
  })
    .then((response) => response.json())
    .catch((error) => console.log(error));

  title.value = "";
  rating.value = 1;
  getMovies();
}