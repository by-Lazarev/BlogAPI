from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from shutil import copyfileobj

router = APIRouter(
    prefix="/file",
    tags=["file"]
)


@router.post("")
def post_file(file: UploadFile = File(...)):
    path = f"files/{file.filename}"
    with open(path, 'w+b') as buffer:
        copyfileobj(file.file, buffer)

    return {
        "filename": path,
        "type": file.content_type
    }


@router.get("/download/{file_name}", response_class=FileResponse)
def get_file(file_name: str):
    path = f"files/{file_name}"
    return path
