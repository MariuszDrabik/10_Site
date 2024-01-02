from typing import Dict
import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from conf_dirs import ROOT_DIR
from database.config import settings
from database.database import POSTGRES_URL
from modules.articles import article_routers
from modules.users import user_routers
from modules.files import files_routers
from oauth import authentication, admin

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=f"{ROOT_DIR}/static"),
    name="static",
)
router = APIRouter()

app.include_router(authentication.router)
app.include_router(files_routers.router)
app.include_router(user_routers.router)
app.include_router(article_routers.router)
app.include_router(admin.router)


@app.get("/")
async def health_checker(test: str = "", test_2: str = "") -> Dict[str, str]:
    print(POSTGRES_URL)
    print(settings.POSTGRES_HOST)
    return {"message": f"Hello from FastAPI {test_2 or ''} {test}"}


origins = ["http://localhost:3233"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1,
        proxy_headers=True,
    )
