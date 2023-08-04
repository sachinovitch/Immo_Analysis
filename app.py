from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
from src.preprocessing import InputData, preprocess_new_data

#uvicorn app:app --reload
# python -m uvicorn app:app --reload

app = FastAPI(debug=True)

pickle_in = open("models/decision_tree.pickle", "rb") # load model in python (rb: read binary)
decisiontree_loaded = pickle.load(pickle_in) 

# http://127.0.0.1:8000
@app.get("/")
def read_root():
    return {
        "message": "Provide the appropriate values of the property",
        "total_property_area": "integer",
        "number_of_facades": "integer",
        "number_of_bedrooms": "integer",
        "state_of_the_building": "true | false",
        "furnished": "true | false",
        "open_fire": "true | false",
        "terrace": "true | false",
        "garden": "true | false",
        "swimming_pool": "true | false",
        "province_choices": "Antwerp | Brussels | East_Flanders | Flemish_Brabant | Walloon_Brabant | Hainaut | Limburg |Liège | Luxembourg | Namur | West_Flanders",
        "subtype_choices": "APARTMENT | APARTMENT_BLOCK | BUNGALOW | CASTLE | CHALET | COUNTRY_COTTAGE | DUPLEX | EXCEPTIONAL_PROPERTY | FARMHOUSE | FLAT_STUDIO | GROUND_FLOOR | HOUSE | KOT | LOFT | MANOR_HOUSE | MANSION | MIXED_USE_BUILDING | OTHER_PROPERTY | PENTHOUSE | SERVICE_FLAT | TOWN_HOUSE | TRIPLEX | VILLA"}

@app.post("/predict/")
def predict_price(data: InputData):
    try:
        # create feature vector
        Feature_Vector = preprocess_new_data(data)
        prediction = decisiontree_loaded.predict(Feature_Vector)
        return {"prediction": "€"+str(prediction[0]),
                    "status_code": "200"} # return predicted price in euro
    
    except TypeError:
          return {"error": "TypeError",
                  "status_code": "400"}
    except KeyError as e:
          return {"error": f"11 fields expected. You forgot: {e}.",
                  "status_code": "400"}
