from typing import Union
from fastapi import FastAPI, File, HTTPException

import json
from readmrz import MrzDetector, MrzReader
import cv2
import numpy as np

import face_recognition
import PIL.Image
from io import BytesIO

def read_cv_img(file):        
        image = None

        try:    
            # response content to numpy array
            arr = np.array(bytearray(file), dtype=np.uint8)

            # decode image
            image = cv2.imdecode(arr, -1)
        except Exception as e:
            #raise Exception(e) from e
            raise HTTPException(status_code=404, detail="Error reading file for MRZ detection: {}".format(e))

        return image

def read_np_img(file):        
        arr = None
               
        try:  
            # read image file
            image = PIL.Image.open(BytesIO(file))
            #convert it to np
            arr = np.array(image)
            
        except Exception as e:            
            raise HTTPException(status_code=404, detail="Error reading file for face recognition: {}".format(e))

        return arr
        
app = FastAPI()

@app.post("/passport_kyc/")
async def create_file(
        passport: Union[bytes, None] = File(default=None),
        photo: Union[bytes, None] = File(default=None),
        ):
    if not passport:
        return {"message": "No passport sent"}

    if not photo:
        return {"message": "No upload file sent"}
    
    #Detect and read MRZ    
    detector = MrzDetector()
    reader = MrzReader()

    image = read_cv_img(passport)
    cropped = detector.crop_area(image)
    
    try:
        result = reader.process(cropped)       
    except Exception as e:
        raise HTTPException(status_code=404, detail="Error in MRZ detection: {}".format(e))  

    #Compare passport and users photo
    passport_image = read_np_img(passport)
    photo_image = read_np_img(photo)
    
    passport_encoding = face_recognition.face_encodings(passport_image)[0]
    photo_encoding = face_recognition.face_encodings(photo_image)[0]
    
    face_results = face_recognition.compare_faces([passport_encoding], photo_encoding)    
    
    [res] = face_results
    
    #add result of comparing to response
    result['person_equality'] = 'equal' if res==True else 'different'
           
    return result   
