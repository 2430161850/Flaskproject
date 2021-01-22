from flask import Flask, url_for, render_template

instance = Flask(__name__)


@instance.route("/")
def index():
    name = "张大炮"
    age = '18'
    sex = '女'
    return render_template('index.html', **locals())


@instance.route("/<int:pk>/")
def detail(pk):
    return f'Flask框架详情{pk}页'


if __name__ == '__main__':
    instance.run(host='192.168.11.10', port='8890', debug=True, )
