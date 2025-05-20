from fastapi import APIRouter, Depends, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.app.models.schemas import MonitoringRequest, MonitoringResponse
from src.app.services.prompt_service import PromptService
from src.app.utils.error_handlers import handle_aws_errors

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.post("/monitor", response_model=MonitoringResponse)
@handle_aws_errors
@limiter.limit("10/minute")
async def monitor_resources(
    request: Request,
    monitoring_request: MonitoringRequest,
    prompt_service: PromptService = Depends()
):
    return await prompt_service.process_request(
        monitoring_request.prompt,
        monitoring_request.region,
        request.client.host,
        monitoring_request.detailed
    )
