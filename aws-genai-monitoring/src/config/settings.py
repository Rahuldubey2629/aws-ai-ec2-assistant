from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_default_region: str = "us-east-1"
    model_name: str = "gpt-4-1106-preview"
    max_retries: int = 3
    temperature: float = 0.2
    script_timeout: int = 30
    cache_ttl: int = 300
    max_prompt_length: int = 1000
    allowed_regions: list = [
        'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2',
        'eu-west-1', 'eu-central-1', 'ap-southeast-1', 'ap-northeast-1'
    ]

    class Config:
        env_file = ".env"

settings = Settings()
