import re
from src.config import settings

FORBIDDEN_ACTIONS = [
    r'create_', r'delete_', r'update_', r'modify_', r'put_', 
    r'post_', r'terminate', r'stop_', r'start_', r'reboot_',
    r'attach_', r'detach_', r'authorize_', r'revoke_'
]

def validate_prompt_content(prompt: str) -> bool:
    """Validate prompt doesn't contain forbidden operations"""
    prompt_lower = prompt.lower()
    return not any(re.search(pattern, prompt_lower) for pattern in FORBIDDEN_ACTIONS)
