import unittest
import requests
from model import prediction_toxicity, load_model,get_model_prediction

model = load_model('original')
text = 'Fuck you !'

class Test(unittest.TestCase):
    def test_prediction_format(self):
        prediction = prediction_toxicity(model,text)
        print(prediction)
        print(len(prediction))
        self.assertCountEqual(prediction,{'toxicity': 0.99,'severe_toxicity':0.45,'obscene':0.99,'threat':0.003,'insult':0.94,'identity_attack':0.01})


if __name__ == '__main__':
    unittest.main()