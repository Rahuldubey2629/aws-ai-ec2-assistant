from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta
from src.app.core.aws_client import AWSClientManager
from src.config import settings

router = APIRouter()

@router.get("/low-cpu")
async def get_low_cpu_instances(region: str = "us-east-1", threshold: int = 40):
    try:
        ec2 = AWSClientManager.get_client('ec2', region)
        cloudwatch = AWSClientManager.get_client('cloudwatch', region)
        
        instances = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        
        instance_ids = [
            instance['InstanceId']
            for reservation in instances['Reservations']
            for instance in reservation['Instances']
        ]
        
        if not instance_ids:
            return {"message": "No running instances found"}
        
        # Get CPU metrics (simplified for example)
        # Actual implementation would need proper metric handling
        
        return {
            "region": region,
            "threshold": threshold,
            "instance_count": len(instance_ids)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
