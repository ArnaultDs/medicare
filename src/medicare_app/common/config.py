from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache



class Settings(BaseSettings): 

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Postgres 
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "football"
    postgres_user: str
    postgres_password: str

    # Minio
    minio_pipeline_access_key: str
    minio_pipeline_secret_key: str 
    minio_bronze_bucket: str
    minio_silver_bucket: str
    minio_endpoint_url: str = "http://localhost:9000"

    @property
    def postgres_database_url(self) -> str: 
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@cache
def get_settings() -> Settings: 
    """ Get app definition from env """
    return Settings() # pyright: ignore[reportCallIssue]