from datetime import datetime
import hashlib
import logging
from src.app.models.schemas import MonitoringResponse
from src.app.services.script_generator import ScriptGenerator
from src.app.services.validation_service import validate_prompt_content
from src.app.core.aws_executor import execute_script

logger = logging.getLogger(__name__)

class PromptService:
    def __init__(self):
        self.script_generator = ScriptGenerator()

    async def process_request(self, prompt: str, region: str, client_ip: str, detailed: bool = False):
        request_id = self._generate_request_id(prompt, region)
        self._log_audit_entry(request_id, prompt, region, client_ip)

        is_valid, warnings = validate_prompt_content(prompt)
        if not is_valid:
            return self._build_error_response(request_id, "Invalid prompt", warnings)

        try:
            generated_script = self.script_generator.generate_script(prompt, region)
            execution_results = execute_script(generated_script, region)
            return MonitoringResponse(
                request_id=request_id,
                status="success",
                generated_script=generated_script if detailed else None,
                execution_results=execution_results,
                warnings=warnings
            )
        except Exception as e:
            return self._build_error_response(request_id, str(e), warnings)

    def _generate_request_id(self, prompt: str, region: str) -> str:
        return hashlib.md5(f"{prompt}-{region}-{datetime.now().timestamp()}".encode()).hexdigest()

    def _log_audit_entry(self, request_id: str, prompt: str, region: str, client_ip: str):
        logger.info(f"AUDIT: {request_id} - {region} - {client_ip}")

    def _build_error_response(self, request_id: str, error: str, warnings: list):
        return MonitoringResponse(
            request_id=request_id,
            status="error",
            error=error,
            warnings=warnings
        )
