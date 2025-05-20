from fastapi import FastAPI
from src.config import settings
from src.app.api.v1.routers import monitor, ec2
from src.app.utils.error_handlers import add_exception_handlers
from src.config.logging_config import configure_logging

app = FastAPI(
    title="AWS Cloud Monitoring Assistant",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)

# Configure logging
configure_logging()

# Add exception handlers
add_exception_handlers(app)

# Include routers
app.include_router(monitor.router, prefix="/api/v1")
app.include_router(ec2.router, prefix="/api/v1/ec2")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
