from fastapi import FastAPI

from src.change.router import router as change_router
from src.delete.router import router as delete_router
from src.info.router import router as info_router
from src.upload.router import router as upload_router
from src.watch.router import router as watch_router

app = FastAPI(title="Video Hosting")

app.include_router(change_router, prefix="/change")
app.include_router(delete_router, prefix="/delete")
app.include_router(info_router, prefix="/info")
app.include_router(upload_router, prefix="/upload")
app.include_router(watch_router, prefix="/watch")
