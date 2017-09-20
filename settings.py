from flask import Flask
app = Flask("DIDSYS")

from playhouse.sqlite_ext import SqliteExtDatabase
db = SqliteExtDatabase("tmp/test.db")