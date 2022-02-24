import pandas as pd 
from detoxify import Detoxify

def load_model(model_name):
    """
    model_name : string - name of the model (original, unbiased, multilingual)
    
    Returns : load the model 
    """
    return Detoxify(model_name)


def prediction_toxicity(model,text):
    """
    model : pre-trained model (original, unbiased,multilingual)
    text : input text we want to predict toxicity
    
    Returns : Score of the toxicity for each label
    """
    prediction = model.predict(text)
    return prediction 

def get_model_prediction(model,text):
    """
    model: pre-trained model (original, unbiased,multilingual)
    text : input text we want to predict toxicity 
    
    Returns : Best score of toxicity
    """
    pred = prediction_toxicity(model,text)
    max_pred = max(pred, key=pred.get)
    return max_pred, pred[max_pred]

if __name__ == '__main__':
    print('Prediction')
    model_name = 'original'
    text = 'Fuck You !'
    model = load_model(model_name)
    p = get_model_prediction(model,text)
    print(p)