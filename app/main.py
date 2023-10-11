from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, select

DATABASE_URL = "mysql+mysqldb://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

some_table = Table("some_table", metadata, autoload_with=engine)

app = FastAPI()

@app.get("/")
def read_root():
    with engine.connect() as connection:
        result = connection.execute(select([some_table])).first()
        return {"message": result["some_field"]}

@app.get("/version")
def get_version():
    return {"version": "1.0", "message": "This is a new change for testing auto-deployment!"}

