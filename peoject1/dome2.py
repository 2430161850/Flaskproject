from flask import Flask

instance = Flask(__name__)


@instance.route("/")
def index():
    return 'Flask框架的首页'


@instance.route("/<int:pk>/")
def detail(pk):
    return f'Flask框架详情{pk}页'


if __name__ == '__main__':
    instance.run(host='192.168.11.10', port='8890', debug=True, )
