import unittest
import requests

class Test(unittest.TestCase):
    def test_response_time(self):
        data = {'text':'Fuck your self, i hope you will die !'}
        response = requests.post('http://back:8000/get_toxicity/', data)
        print(response.elapsed.total_seconds())
        self.assertLessEqual(response.elapsed.total_seconds(), 1) 

    def test_response(self):
        resp = requests.get('http://back:8000/')
        self.assertEqual(resp.status_code, 200)

    def test_stress(self):
        for i in range(1000):
            resp = requests.get('http://back:8000/')
            self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()