# the pickle lib is used to load the machine learning model
import pickle
import pandas as pd


class HousePriceModel():

    def __init__(self):
        self.model = self.load_model()
        self.preds = None

    def load_model(self):
        # uses the file model.pkl
        pkl_filename = 'model.pkl'

        try:
	    pickle.load(open(filename, 'rb'))
 # or         with open(pkl_filename, 'rb') as file:
 #               pickle_model = pickle.load(file)
        except:
            print(f'Error loading the model at {pkl_filename}')
            return None

        return pickle_model

    def predict(self, data):

        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data, index=[0])

        # makes the predictions using the loaded model
        self.preds = self.model.predict(data)
        return self.preds