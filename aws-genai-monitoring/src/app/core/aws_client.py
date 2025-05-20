import boto3
from src.config import settings

class AWSClientManager:
    _instances = {}

    @classmethod
    def get_client(cls, service_name: str, region: str = None):
        region = region or settings.aws_default_region
        cache_key = f"{service_name}:{region}"
        
        if cache_key not in cls._instances:
            cls._instances[cache_key] = boto3.client(
                service_name,
                aws_access_key_id=settings.aws_access_key_id,
                aws_secret_access_key=settings.aws_secret_access_key,
                region_name=region
            )
        return cls._instances[cache_key]
