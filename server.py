from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

prof = ['пилот', 'биолог', 'инженер', 'психолог', 'священник']
num = 1


@app.route('/list_prof/<list>')
def index(list):
    return render_template('base.html', list=list, prof=prof, num=num)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
