from flask import json

from app import app

test_data = {
    "ID": 1,
    "LicAge": 468,
    "RecordBeg": "2004-01-01",
    "RecordEnd": "",
    "VehAge": 100,
    "Gender": "Male",
    "MariStat": "Other",
    "SocioCateg": "CSP50",
    "VehUsage": "Private",
    "DrivAge": 5,
    "HasKmLimit": 0,
    "BonusMalus": 56,
    "OutUseNb": 0,
    "RiskArea": 0
}


def test_ml_api():
    response = app.test_client().post(
        '/predict',
        data=json.dumps(test_data),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["ID"] == 1
    assert data["value_BurningCost"] == 147.37984322575497
    assert data["value_Gamma"] == 711.1153561524523
    assert data["value_Poisson"] == 0.2072516673288644
