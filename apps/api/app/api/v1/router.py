from app.api.v1.system import router as system_router
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")
router.include_router(system_router)
