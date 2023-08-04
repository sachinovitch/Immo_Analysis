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
        "province_choices": list(ProvinceEnum),'Antwerp'|'Brussels'|'East_Flanders'|'Flemish_Brabant'|'Walloon_Brabant'|'Hainaut'|'Limburg'|'Liège'|'Luxembourg'|'Namur'|'West_Flanders'
        "subtype_choices": list(SubtypeEnum),
    }
# "province_choices": "Antwerp | Brussels | East_Flanders | Flemish_Brabant | Walloon_Brabant | Hainaut | Limburg |Liège | Luxembourg | Namur | West_Flanders"
# def read_root():
#     return {"message": "provide the appropriate values of the property",
#             "'total_property_area', 'number_of_facades' and 'number_of_bedrooms' require an integer as value","'state_of_the building', 'furnished', 'open_fire', 'terrace' and 'garden' require a boolean value 'true' or 'false'",
#             return {
#         "message": "Provide the appropriate values of the property",
#         "province_choices": list(ProvinceEnum),
#         "subtype_choices": list(SubtypeEnum),}
#     }
    #"message": "'province' takes one of these strings: 'Antwerp', 'Brussels', 'East_Flanders', 'Flemish_Brabant', 'Walloon_Brabant', 'Hainaut', 'Limburg', 'Liège', 'Luxembourg', 'Namur', 'West_Flanders'",
            #"message": "'subtype' takes one of these strings: 'APARTMENT','APARTMENT_BLOCK','BUNGALOW','CASTLE','CHALET','COUNTRY_COTTAGE','DUPLEX','EXCEPTIONAL_PROPERTY','FARMHOUSE','FLAT_STUDIO','GROUND_FLOOR','HOUSE','KOT','LOFT','MANOR_HOUSE','MANSION','MIXED_USE_BUILDING','OTHER_PROPERTY','PENTHOUSE','SERVICE_FLAT','TOWN_HOUSE','TRIPLEX','VILLA'"
            
@app.post("/predict/")
def predict_price(data: InputData):
    try:
        # create feature vector
        X = preprocess_new_data(data)
        prediction = decisiontree_loaded.predict(X)
        return {"prediction": "€"+str(prediction[0]),
                    "status_code": "200"} # return predicted price in euro
    except TypeError:
          return {"error": "TypeError"}
    except KeyError as e:
          return {"error": f"11 fields expected. You forgot: {e}."}
