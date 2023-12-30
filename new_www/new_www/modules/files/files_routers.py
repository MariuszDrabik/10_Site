from typing import Dict
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from conf_dirs import ROOT_DIR


router = APIRouter(prefix="/attachments", tags=["attachments"])


@router.get("/{id}")
async def root(id: int) -> Dict[str, str]:
    return {"image": "img"}


@router.post("/", status_code=201)
async def upload_file(file: UploadFile = File(...)) -> Dict[str, str]:
    directory = "static/images"
    name = file.filename.replace(" ", "_")
    with open(f"{ROOT_DIR}/{directory}/{name}", "wb") as handler:
        handler.write(await file.read())

    return {"file": f"File {file}", "filename": f"{file.filename}"}


@router.get("/download/{name}", response_class=FileResponse)
def get_gile(name: str):
    path = f"{ROOT_DIR}/obrazki/{name}"
    return path
