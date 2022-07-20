# Flask-ML-API

## Пример вывода в продукцию модели машинного обучения

### Установка
Клонирование репозитория
```
git clone https://github.com/MindSetLib/Flask-ML-API.git
cd Flask-ML-API
git checkout vtb-demonstration
```
Создание .env файла
```
touch .env
cat <<EOT > .env
model_path=models/gbm_count.pickle
transforms_path=models/transforms.uu
EOT
```
### Запуск с использованием Docker:
Создание Docker image 
```
docker build -t demonstration . 
```
Запуск приложения
```
docker run -d -p 30000:5000 --name demonstration demonstration
```
### Проверка работоспособности приложения
Healthcheck
```
curl --location --request GET 'http://<your_ip_or_domen>:30000/healthcheck'
```
Predict method
```
curl --location --request POST 'http://<your_ip_or_domen>:30000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"df": {"Exposure":0.224,
        "LicAge":112,
        "RecordBeg":"2004-01-01",
        "RecordEnd":"2004-03-22",
        "Gender":"Male",
        "MariStat":"Alone",
        "SocioCateg":"CSP26",
        "VehUsage":"Private+trip to office",
        "DrivAge":30,
        "HasKmLimit":1,
        "BonusMalus":95,
        "RiskArea":6.0}
}'
```
