from sqlalchemy import create_engine, Column, String, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://app:12345678@127.0.0.1:5431/app')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Ads(Base):

    __tablename__ = "ads_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String, index=True)
    description = Column(String, index=True)
    create_time = Column(DateTime, server_default=func.now())
    user = Column(String, index=True)


Base.metadata.create_all()