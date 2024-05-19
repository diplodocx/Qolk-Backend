import psycopg2 as pg
import config as c

pg_uri = f"postgres://{c.POSTGRES_USER}:{c.POSTGRES_PASSWORD}@{c.POSTGRES_HOST}:{c.POSTGRES_PORT}/{c.POSTGRES_DB}"


def connect():
    conn = pg.connect(pg_uri)
    return conn
