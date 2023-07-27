from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle

#TODO  change class,

#uvicorn API:app --reload

class InputData(BaseModel):
    total_property_area: int
    number_of_facades: int
    number_of_bedrooms: int
    state_of_the_building: bool
    furnished: bool
    open_fire: bool
    terrace: bool
    garden: bool
    swimming_pool: bool
    province: str #categorical
    subtype: str #categorical


app = FastAPI()

pickle_in = open("decision_tree.pickle", "rb") # load model in python (rb: read binary)
decisiontree_loaded = pickle.load(pickle_in) 

# http://127.0.0.1:8000
@app.get("/")
def read_root():
    return {"features": features}

@app.post("/predict/")
def predict_price(data: InputData):
    try:
        X = array([[data["total_property_area"],
                    data["state_of_the_building"].astype(int),
                    data["number_of_facades"],
                    data["number_of_bedrooms"],
                    1 if data["province"] == "Antwerp" else 0,
                    1 if data["province"] == "Brussels" else 0,
                    1 if data["province"] == "East_Flanders" else 0,
                    1 if data["province"] == "Flemish_Brabant" else 0,
                    1 if data["province"] == "Walloon_Brabant" else 0,
                    1 if data["province"] == "Hainaut" else 0,
                    1 if data["province"] == "Limburg" else 0,
                    1 if data["province"] == "Liège" else 0,
                    1 if data["province"] == "Luxembourg" else 0,
                    1 if data["province"] == "Namur" else 0,
                    1 if data["province"] == "West_Flanders" else 0,
                    1 if data["subtype"] == "APARTMENT" else 0,
                    1 if data["subtype"] == "APARTMENT_BLOCK" else 0,
                    1 if data["subtype"] == "BUNGALOW" else 0,
                    1 if data["subtype"] == "CASTLE" else 0,
                    1 if data["subtype"] == "CHALET" else 0,
                    1 if data["subtype"] == "COUNTRY_COTTAGE" else 0,
                    1 if data["subtype"] == "DUPLEX" else 0,
                    1 if data["subtype"] == "EXCEPTIONAL_PROPERTY" else 0,
                    1 if data["subtype"] == "FARMHOUSE" else 0,
                    1 if data["subtype"] == "FLAT_STUDIO" else 0,
                    1 if data["subtype"] == "GROUND_FLOOR" else 0,
                    1 if data["subtype"] == "HOUSE" else 0,
                    1 if data["subtype"] == "KOT" else 0,
                    1 if data["subtype"] == "LOFT" else 0,
                    1 if data["subtype"] == "MANOR_HOUSE" else 0,
                    1 if data["subtype"] == "MANSION" else 0,
                    1 if data["subtype"] == "MIXED_USE_BUILDING" else 0,
                    1 if data["subtype"] == "OTHER_PROPERTY" else 0,
                    1 if data["subtype"] == "PENTHOUSE" else 0,
                    1 if data["subtype"] == "SERVICE_FLAT" else 0,
                    1 if data["subtype"] == "TOWN_HOUSE" else 0,
                    1 if data["subtype"] == "TRIPLEX" else 0,
                    1 if data["subtype"] == "VILLA" else 0,
                    data["furnished"].astype(int),
                    data["open_fire"].astype(int),
                    data["terrace"].astype(int),
                    data["garden"].astype(int),
                    data["swimming_pool"].astype(int),]])
        prediction = decisiontree_loaded.predict(X)
        return {"prediction": "%s"%(u"\N{euro sign}")+str(prediction)} # return price in euro
    except TypeError:
        return {"error": "expected numbers, got strings."}
    except KeyError as e:
        return {"error": f"3 fields expected (salary, bonus, taxes). You forgot: {e}."}

