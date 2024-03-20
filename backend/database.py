from sqlmodel import SQLModel, create_engine, Session
# from service.core.config import settings

# db_name = settings.db_name
# username = settings.db_user
# password = settings.db_password
# host = settings.db_host
# port = settings.db_port

sqlite_file_name = "inventory.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# db_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

