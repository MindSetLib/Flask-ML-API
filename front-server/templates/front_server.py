import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField
from wtforms.validators import DataRequired

from postman import data, send_json


class ClientDataForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    age = IntegerField('Возраст водителя', validators=[DataRequired()])
    lic_age = IntegerField('Водительский стаж', validators=[DataRequired()])
    gender = SelectField('Пол', choices=[('Male', 'М'), ('Female', 'Ж')])
    mari_stat = SelectField('Семейное положение', choices=[('Alone', 'Alone'), ('Other', 'Other')])
    veh_age = IntegerField('Возраст автомобиля', validators=[DataRequired()])
    bonus_malus = IntegerField('Коэффициент BonusMalus', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    if request.method == 'POST':
        data['ID'] = request.form.get('id')
        data['DrivAge'] = float(request.form.get('age'))
        data['LicAge'] = float(request.form.get('lic_age'))
        data['Gender'] = request.form.get('gender')
        data['MariStat'] = request.form.get('mari_stat')
        data['VehAge'] = float(request.form.get('veh_age'))
        data['BonusMalus'] = float(request.form.get('bonus_malus'))
        try:
            response = send_json(data)
            response = response.text
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.2', debug=True)
