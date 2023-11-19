
<pre>
  Title: URL shortener API with FastAPI and SQLite
  Author: Momfer de Mol
  Status: WIP
  Created: 08-09-2023
</pre>

# url-shortener-api

Run program
```sh
$ uvicorn app.main:app --reload
```
> Remove `--reload` when running in production.

**API docs**

Go to `/docs` when app is running for API docs.

**Dependency**

Python modules used in `pyproject.toml`.

**Environment**

Project uses `.env` file to load environment variables which overwrites `/app/config.py`.

**Development**

Local development environment created with `devenv.nix`.