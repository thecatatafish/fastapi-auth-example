# Basic FastAPI Authentication Example

This minimal app allows users to log in and register movies and give them a rating. The movies
and their ratings are stored in a SQLite database and FastAPI serves them via an endpoint only
accessible by the user who added the movie.

In the UI there is also a button to get data from a public endpoint which just returns the time from
FastAPI, to demo that this endpoint is not protected.

By default there are two separate users created, `test1@test.com` and `test2@test.com` and the password is `secret` for both of them. For conveniance the username and password fields are automatically filled in the UI.


## How to run the app

[Install Poetry package manager](https://python-poetry.org/docs/#installation)

In the root folder of this project install dependencies
`poetry install`

Start the backend and serve the frontend by executing
`./start_app.sh`
