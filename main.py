"""
Formula 1 Analytics REST API
Architecture: Controller - Service - Repository (CSR)
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from utils.messages.success_message import SuccessMessage
from utils.messages.error_message import ErrorMessage
from utils.responses.base_response import BaseResponse

# Import Controllers
from controllers.seasons_controller import router as seasons_router
from controllers.circuits_controller import router as circuits_router
from controllers.drivers_controller import router as drivers_router
from controllers.constructors_controller import router as constructors_router
from controllers.races_controller import router as races_router
from controllers.standings_controller import router as standings_router
from controllers.analytics_controller import router as analytics_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Enterprise REST API for Formula 1 Historical Data, Race Weekends, Starting Grids, Standings & Performance Analytics.",
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=BaseResponse.error(
            message=f"{ErrorMessage.INTERNAL_SERVER_ERROR} Details: {str(exc)}"
        ).dict()
    )

# Root Health Check
@app.get("/", response_model=BaseResponse[dict], tags=["System"])
def root():
    return BaseResponse.ok(
        data={"status": "online", "version": settings.PROJECT_VERSION, "docs": "/docs"},
        message=SuccessMessage.HEALTH_CHECK_SUCCESS
    )

# Register All API Routers under /api/v1
app.include_router(seasons_router, prefix=settings.API_V1_PREFIX)
app.include_router(circuits_router, prefix=settings.API_V1_PREFIX)
app.include_router(drivers_router, prefix=settings.API_V1_PREFIX)
app.include_router(constructors_router, prefix=settings.API_V1_PREFIX)
app.include_router(races_router, prefix=settings.API_V1_PREFIX)
app.include_router(standings_router, prefix=settings.API_V1_PREFIX)
app.include_router(analytics_router, prefix=settings.API_V1_PREFIX)
