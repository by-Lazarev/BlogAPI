# BlogAPI
My Instagram like blog API.


***

## To start:
python -m venv blogAPI

source blogAPI/Scripts/activate

pip install -r requirements.txt

## Add config.py files in /auth and /db dirs

- for auth add SECRET_KEY var with var of the
- `openssl rand -hex 32` command


- for db add SQLALCHEMY_DATABASE_URL var with var
- `dialect+driver://username:password@host:port/database
`
- more information https://fastapi.tiangolo.com/tutorial/sql-databases/