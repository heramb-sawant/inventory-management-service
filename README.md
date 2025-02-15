# Inventory Management System

Used to help automate inventory management.

## Features

## Installation & Setup

### Get Postgres Running

You could always set up Postgres yourself but this repo has a Postgres container setup and ready to use!

1. [Install docker]([url](https://docs.docker.com/get-started/get-docker/))
2. run `docker compose up` in your cli
3. ✨ Done ✨

If you want to access the postgres instance in the docker container:
1. `docker ps`
2. copy the Container Id
3. `docker exec -it {container_id} bash`
4. `psql -U {username}` The default env username is `admin`

Some helpful Postgres commands
- `\du` list users
- `\dt` list tables
- `\l` list databases

### Start Django App

- Instructions on things to install and what they are used for
- Use `uv` to manage packages & dependencies
- Use `ruff` to manage linting
- Use `ruff` to manage auto formatting
- Use `mypy` to manage a type system
- You have to install the CLI and vscode extension to get it all working
- Auto save settings

- `uv add {package}` to add a package to the project
- `uv add --dev {package}` to add a dev dependency to the project
- `uv remove {package}` to remove a package from the project
- `uv run {package} {directory}` to run commands
- `ruff check` to run linter

## Running The Server

## Testing

`python manage.py {app} test` - run test in an app

TODO

- Split tests into unit and integration
- Split tests into more than one file
- Get tests working on a docker test container

## Migration

- `python manage.py makemigrations {app}` - create migrations for a file
- `python manage.py sqlmigrate {app} {migration_number}` - view what migration will be run
- `python manage.py migrate` - apply migration2

TODO:

- Add some custom scripts to automate a few things
  - Migrate:create|up|down
  - Automatically sync db with code when starting or running tests locally
  - Seed scripts

## Project TODO

- Delete the db/repository & try to make installing it easy as possible
- Environment variables
- Database design, levels of normalization, etc…
- Authentication/middleware
- ASGI vs WSGI. Apache vs Django wsgi

### Github

- Pipeline
  - Tests
  - Linter
  - Type Checker
- Enforce PR requests
- Set up code owners
- Dependabot

## Dev Standards

- Error Class & Standards
- Standardize file structure
- Figure out logging
- Pre commit hooks?
