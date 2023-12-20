from sqlalchemy import create_engine
from settings import USER, PASSWORD, HOST, PORT, DATABASE_NAME

# Membuat koneksi menggunakan SQLAlchemy
engine = create_engine(
    f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
)