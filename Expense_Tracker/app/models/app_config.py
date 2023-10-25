from sqlalchemy import Column, String, Integer
from app.models import Base


class ConfigParams(Base):
    __tablename__ = 'app_config_master'

    config_id = Column(Integer, primary_key=True, autoincrement=True)
    enc_key = Column('enc_key', String(100), nullable=False)
