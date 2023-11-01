import logging
from typing import Dict
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
import uvicorn
from conf_dirs import ROOT_DIR
from database.config import settings, oko

# from database.config import settings

app = FastAPI()

app.mount(
    f"/static",
    StaticFiles(directory=f"{ROOT_DIR}/static"),
    name="static",
)
router = APIRouter()


@app.get("/")
async def root(oko_id: str | None = None, ne: str | None = None) -> Dict[str, str]:
    print(settings.POSTGRES_HOSTNAME)
    print(settings.POSTGRES_HOST)
    # breakpoint()
    oko()
    return {f"message": f"Hello from FastAPI {ne or ''} {oko_id}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1,
        proxy_headers=True,
    )
