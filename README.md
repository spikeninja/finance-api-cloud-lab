## Installation

Install all dependencies by **pip**:

```shell
pip install -r requirements.txt
```

or install all dependencies by **pipenv**:

```shell
pipenv install

# and then activate virtual environment
pipenv shell
```

## Running
1) Run below line to run all containers:

```shell
docker-compose up
```

2) Run below line to create all tables in db:

```shell
docker exec -it cloud_pgsql_dev psql -U cloud_user -d cloud_db -f misc/createdb.sql
```
