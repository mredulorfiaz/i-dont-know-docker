import os
DB_PASS = os.getenv("DB_PASS", "root")
DB_HOST = os.getenv("DB_HOST", "db")

CONFIGURATION = {
    "track": "SQLALCHEMY_TRACK_MODIFICATIONS",
    "uri": "SQLALCHEMY_DATABASE_URI",
    "sqlite": "sqlite:///usersdb.sqlite",
    "host": "0.0.0.0",
    "mysql": f"mysql+pymysql://root:{DB_PASS}@{DB_HOST}/users_db",
}
