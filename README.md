# Inventory Management System

Used to help automate inventory management.

## Features

## Installation & Setup

Steps I had to take to get a db running

- Start db
  - Install postgres through brew
  - Brew services start postgresql
- Create db
  - `createdb inventory_management`- Create a db
  - `psql inventory_management`- Start a shell
  - `\c inventory_management` - Connect to a db
- Create users for db
  - `\du` display user roles
  - CREATE USER test WITH PASSWORD 'testpassword';
  - GRANT ALL PRIVILEGES ON DATABASE inventory_management TO test;
  - `\l+` for db level PRIVILEGES
- Other commands I used
  - `\dt` list tables
  - `\du` list users
  - DROP USER testUser;
- Finished creating/setting up the db by update settings.py with the db information
- Ran `python manage.py migrate` to make sure everything looked good

  TODO:

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
- `python manage.py migrate` - apply migration

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
