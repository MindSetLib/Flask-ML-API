import requests

data = {
    "ID": 1,
    "LicAge": 468,
    "RecordBeg": "2004-01-01",
    "RecordEnd": "",
    "VehAge": "",
    "Gender": "Male",
    "MariStat": "Other",
    "SocioCateg": "CSP50",
    "VehUsage": "Private",
    "DrivAge": 67,
    "HasKmLimit": 0,
    "BonusMalus": 56,
    "OutUseNb": 0,
    "RiskArea": 0
}


def send_json(data):
    url = 'http://127.0.0.1:5000/predict'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response


if __name__ == '__main__':
    response = send_json(data)
    print(response.json())
