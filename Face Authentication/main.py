from fastapi import FastAPI, UploadFile, File, HTTPException
from deepface import DeepFace
import os
import shutil

app = FastAPI(title="Face Authentication API")

UPLOAD_DIR = "temp_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/verify")
async def verify_faces(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    
    if not file1.filename or not file2.filename:
        raise HTTPException(status_code=400, detail="Please upload two image files.")

    path1 = f"{UPLOAD_DIR}/{file1.filename}"
    path2 = f"{UPLOAD_DIR}/{file2.filename}"

    with open(path1, "wb") as buffer1:
        shutil.copyfileobj(file1.file, buffer1)
    with open(path2, "wb") as buffer2:
        shutil.copyfileobj(file2.file, buffer2)

    try:
        result = DeepFace.verify(img1_path=path1, img2_path=path2, enforce_detection=True)

        status_text = "same person" if result["verified"] else "different person"

        response = {
            "verification_result": status_text,
            "similarity_score": result["distance"],
            "bounding_boxes": {
                "image1": result["facial_areas"]["img1"],
                "image2": result["facial_areas"]["img2"]
            }
        }
        
        os.remove(path1)
        os.remove(path2)
        return response

    except Exception as e:
        if os.path.exists(path1): os.remove(path1)
        if os.path.exists(path2): os.remove(path2)
        raise HTTPException(status_code=500, detail=str(e))