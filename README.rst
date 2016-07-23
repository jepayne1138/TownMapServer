Town Map Server
===============

Description
-----------
Runs the server for the Town Map app. Manages queries and updates to the database through and exposed API.

Use
---
*Coming soon...*

Installation
------------
*Coming soon...*

Instructions
------------
Useful heroku toolbelt commands::

    heroku login
    heroku create <project>
    git remote heroku git@heroku.com:<project>.git
    heroku ps:scale web=1
    heroku logs --tail
    heroku addons:create heroku-postgresql:hobby-dev
    heroku config:set <config1>=<value1> <config2>=<value2>


Remember to create an .env file and populate it with the following::

    DATABASE_URL=postgres://<host>/<local database name>
    HOST=0.0.0.0
    PORT=5000


Populating Heroku database from local Postgresql database (Powershell)::

    pg_dump -f <sql file> -U <username> <local table name>
    heroku pg:reset
    get-content <sql file> | heroku pg:pgsql --app <heroku project>
