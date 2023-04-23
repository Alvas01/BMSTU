import flask
import tensorflow as tf
import pickle

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods = ['POST', 'GET'])
def index():
    return flask.render_template('index.html')

@app.route('/main_1', methods = ['POST', 'GET'])
def main_1():
    result_1 = ''
    if flask.request.method == 'GET':
        return flask.render_template('main_1.html')
    if flask.request.method == 'POST':
        param_list = ('Соотношение матрица-наполнитель', 'Плотность, кг/м3', 'модуль упругости, ГПа', 'Количество отвердителя, м.%',
                      'Содержание эпоксидных групп,%_2', 'Температура вспышки, С_2', 'Поверхностная плотность, г/м2', 
                      'Потребление смолы, г/м2', 'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки')
        params = []
        for i in param_list:
            param = flask.request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        with open('best_model_1.pkl', 'rb') as f:
            model = pickle.load(f)

        pred = model.predict([params])

        result_1 = f'Модуль упругости при растяжении, ГПа: {pred}'
        return flask.render_template('main_1.html', result=result_1)

@app.route('/main_2', methods = ['POST', 'GET'])
def main_2():
    result_2 = ''
    if flask.request.method == 'GET':
        return flask.render_template('main_2.html')
    if flask.request.method == 'POST':
        param_list = ('Соотношение матрица-наполнитель', 'Плотность, кг/м3', 'модуль упругости, ГПа', 'Количество отвердителя, м.%',
                      'Содержание эпоксидных групп,%_2', 'Температура вспышки, С_2', 'Поверхностная плотность, г/м2', 
                      'Потребление смолы, г/м2', 'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки')
        params = []
        for i in param_list:
            param = flask.request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        with open('best_model_2.pkl', 'rb') as f:
            model = pickle.load(f)

        pred = model.predict([params])

        result_2 = f'Прочность при растяжении, МПа: {pred}'
        return flask.render_template('main_2.html', result=result_2)
    
@app.route('/main_3', methods = ['POST', 'GET'])
def main_3():
    result_3 = ''
    if flask.request.method == 'GET':
        return flask.render_template('main_3.html')
    if flask.request.method == 'POST':
        param_list = ('Плотность, кг/м3', 'модуль упругости, ГПа', 'Количество отвердителя, м.%',
                      'Содержание эпоксидных групп,%_2', 'Температура вспышки, С_2', 'Поверхностная плотность, г/м2', 
                      'Модуль упругости при растяжении, ГПа', 'Прочность при растяжении, МПа', 'Потребление смолы, г/м2',
                      'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки')
        params = []
        for i in param_list:
            param = flask.request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        model = tf.keras.models.load_model('models/ANN')
        pred = model.predict([params])

        result_3 = f'Соотношение матрица-наполнитель: {pred}'
        return flask.render_template('main_3.html', result=result_3)

if __name__ == '__main__':
    app.run()