from pydantic import BaseSettings


class Settings(BaseSettings):
    token_id: str
    token_secret:  str
    basic_auth: str
    
    class Config:
        env_file = '.env'

