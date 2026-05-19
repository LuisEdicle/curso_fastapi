from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """_
        Configuracoes gerais usadas na aplicacao
    """

    API_v1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://geek:university@localhost:5432/faculdade"
    DBBaseModel = declarative_base

    class Config:
        case_sensitive = True
    
settings = Settings()