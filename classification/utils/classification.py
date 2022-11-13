from core.messages import CoreMessage
from classification.models import predict, features
from typing import NoReturn

class Classification(object):
    def __init__(self,data):
        self._error = 0
        self.data = data

        if self._error == 0:
            self.__process()
        
    def fit(self):
        try:
            if self._error == 0:
                return self._data_response, self._error
            else:
                return self._msg, self._error
        except Exception as e:
            self._logError += "Error (data):" + str(e)
            self.__ErroLog()

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, data: str) -> NoReturn:
        features_list = ["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"]
        if not all(x in data for x in features_list):
            self._msg, self._error = "Invalid data input format.", 1
            self._data = data    
        else:
            self._data = data

    def __process(self):
        try:
            self.__input_data()
        except Exception:
            self._msg, self._error = CoreMessage().server_error, 1
        

    def __input_data(self):
        try:
            feat_db = features()
            feat_db.V1 = self._data["V1"]
            feat_db.V2 = self._data["V2"]
            feat_db.V3 = self._data["V3"]
            feat_db.V4 = self._data["V4"]
            feat_db.V5 = self._data["V5"]
            feat_db.V6 = self._data["V6"]
            feat_db.V7 = self._data["V7"]
            feat_db.V8 = self._data["V8"]
            feat_db.V9 = self._data["V9"]
            feat_db.V10 = self._data["V10"]
            feat_db.V11 = self._data["V11"]
            feat_db.V12 = self._data["V12"]
            feat_db.V13 = self._data["V13"]
            feat_db.V14 = self._data["V15"]
            feat_db.V15 = self._data["V15"]
            feat_db.V16 = self._data["V16"]
            feat_db.V17 = self._data["V17"]
            feat_db.V18 = self._data["V18"]
            feat_db.V19 = self._data["V19"]
            feat_db.V20 = self._data["V20"]
            feat_db.V21 = self._data["V21"]
            feat_db.V22 = self._data["V22"]
            feat_db.V23 = self._data["V23"]
            feat_db.V24 = self._data["V24"]
            feat_db.V25 = self._data["V25"]
            feat_db.V26 = self._data["V26"]
            feat_db.V27 = self._data["V27"]
            feat_db.V28 = self._data["V28"]
            feat_db.Amount = self._data["Amount"]
            feat_db.save()

            pred_db = predict()
            pred_db.model = "Random Forest"
            pred_db.class_predicted = 0
            pred_db.probability = [0.1,0.9]
            pred_db.featuresid = feat_db
            pred_db.save()

            self._data_response = {
                                    "id": pred_db.id,
                                    "class": pred_db.class_predicted,
                                    "probability": pred_db.probability
                                    }

        except Exception as e:
            self._msg, self._error = CoreMessage().server_error, 1