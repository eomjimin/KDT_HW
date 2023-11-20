# pip install python-multipart

from fastapi import FastAPI, File, UploadFile
import shutil 
import os
app = FastAPI()

@app.post("/uploadnsave")
async def create_upload_file(file: UploadFile):
    if not file:
        return {"message": "파일이 존재하지 않음"}
    else:
        dir_path = os.path.join("C:\\jimin\\KDT\\FastAPI", file.filename)
        with open(dir_path, "wb") as target:
            shutil.copyfileobj(file.file, target)
