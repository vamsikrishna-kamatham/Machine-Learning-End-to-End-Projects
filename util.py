# importing necessary libraries and modules
import pickle
import json
import numpy as np

# initializing variables
__locations = None
__data_columns = None
__model = None

# function to get estimated price based on location, square feet, BHK, and bathrooms
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower()) # get index of the location
    except:
        loc_index = -1 # set default index to -1

    x = np.zeros(len(__data_columns)) # initialize input array with zeros
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1 # set the location value to 1 if found in data columns

    return round(__model.predict([x])[0],2)

# function to load saved artifacts
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    # Load data columns
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model

    # Load saved model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

# function to get location names
def get_location_names():
    return __locations

# function to get data columns
def get_data_columns():
    return __data_columns

# main block of code to test the functions
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location