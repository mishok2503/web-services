from fastapi import FastAPI

from .routers.change.router import router as change_router
from .routers.delete.router import router as delete_router
from .routers.info.router import router as info_router
from .routers.upload.router import router as upload_router
from .routers.watch.router import router as watch_router

app = FastAPI(title="Video Hosting")

app.include_router(change_router, prefix="/change")
app.include_router(delete_router, prefix="/delete")
app.include_router(info_router, prefix="/info")
app.include_router(upload_router, prefix="/upload")
app.include_router(watch_router, prefix="/watch")
