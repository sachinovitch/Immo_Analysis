from pydantic import BaseModel
from enum import Enum

class ProvinceEnum(str, Enum):
    Antwerp = "Antwerp"
    Brussels = "Brussels"
    East_Flanders = "East_Flanders"
    Flemish_Brabant = "Flemish_Brabant"
    Walloon_Brabant = "Walloon_Brabant"
    Hainaut = "Hainaut"
    Limburg = "Limburg"
    Liège = "Liège"
    Luxembourg = "Luxembourg"
    Namur = "Namur"
    West_Flanders = "West_Flanders"

class SubtypeEnum(str, Enum):
    APARTMENT = "APARTMENT"
    APARTMENT_BLOCK = "APARTMENT_BLOCK"
    BUNGALOW = "BUNGALOW"
    CASTLE = "CASTLE"
    CHALET = "CHALET"
    COUNTRY_COTTAGE = "COUNTRY_COTTAGE"
    DUPLEX = "DUPLEX"
    EXCEPTIONAL_PROPERTY = "EXCEPTIONAL_PROPERTY"
    FARMHOUSE = "FARMHOUSE"
    FLAT_STUDIO = "FLAT_STUDIO"
    GROUND_FLOOR = "GROUND_FLOOR"
    HOUSE = "HOUSE"
    KOT = "KOT"
    LOFT = "LOFT"
    MANOR_HOUSE = "MANOR_HOUSE"
    MANSION = "MANSION"
    MIXED_USE_BUILDING = "MIXED_USE_BUILDING"
    OTHER_PROPERTY = "OTHER_PROPERTY"
    PENTHOUSE = "PENTHOUSE"
    SERVICE_FLAT = "SERVICE_FLAT"
    TOWN_HOUSE = "TOWN_HOUSE"
    TRIPLEX = "TRIPLEX"
    VILLA = "VILLA"

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
    province: ProvinceEnum
    subtype: SubtypeEnum
    
    
def preprocess_new_data(data: InputData):
    '''transform input data into feature vector'''
    X = [[data.total_property_area,
          data.state_of_the_building,
          data.number_of_facades,
          data.number_of_bedrooms,
          *[1 if data.province == province_enum else 0 for province_enum in ProvinceEnum],
          *[1 if data.subtype == subtype_enum else 0 for subtype_enum in SubtypeEnum],
          data.furnished,data.open_fire,
          data.terrace,
          data.garden,
          data.swimming_pool]]
    return X

# app = FastAPI(debug=True)

# pickle_in = open("models/decision_tree.pickle", "rb")
# decisiontree_loaded = pickle.load(pickle_in)

# @app.get("/")
# def read_root():
#     return {
#         "message": "Provide the appropriate values of the property",
#         "province_choices": list(ProvinceEnum),
#         "subtype_choices": list(SubtypeEnum),
#     }

# @app.post("/predict/")
# def predict_price(data: InputData):
#     # Get the list of required fields in the InputData model
#     required_fields = set(data.__fields__.keys())
#     # Get the list of provided fields in the input data
#     provided_fields = set(data.dict().keys())

#     # Check for missing fields
#     missing_fields = required_fields - provided_fields
#     if missing_fields:
#         return {"message": "Some fields are missing or have incorrect values.",
#                 "missing_fields": list(missing_fields)}

#     try:
#         # create feature vector
#         X = preprocess_new_data(data)
#         prediction = decisiontree_loaded.predict(X)
#         return {"prediction": "€" + str(prediction[0]),
#                 "status_code": 200}
#     except TypeError:
#         raise HTTPException(status_code=400, detail="Bad Request")
#     except KeyError as e:
#         raise HTTPException(status_code=400, detail=f"Field missing: {e}")
