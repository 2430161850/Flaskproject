from flask import Flask, url_for, render_template

instance = Flask(__name__)

book = {
    "name": "国士无双",
    "author": "骁骑校",
    "chapter": [
        {
            "id": 101,
            "name": "邂逅旧帝都",
            "context": "天阴沉沉的，前门火车站外密密匝匝的停满了人力车和马车，车夫们抄手缩脖，坐在洋车水簸箕的脚垫上东拉西扯着。"
                       "马路边残雪犹在，远处的正阳门箭楼巍峨耸立，呈现着旧帝都的气派与凋敝"
        },
        {"id": 102,
         "name": "关外来的土匪",
         "context": "前门火车站正对着正阳门的城门楼和箭楼，箭楼西侧是正阳门西站，"
                    "京汉线的始发站，夹在两个火车站之间的正阳门广场热"
         },
        {"id": 103,
         "name": "双枪快腿小白龙",
         "context": "我还以为你是逃兵呢，让宪兵队逮着可不是闹着玩的。”小顺子随口道"

         }
    ]
}


@instance.route("/")
def index():
    articles = book["chapter"]
    return render_template('index.html', **locals())


@instance.route("/<int:pk>/")
def detail(pk):
    article = None
    lista = book["chapter"]
    for i in lista:
        if i["id"] == pk:
            article =i
    return render_template('detail.html', **locals())


if __name__ == '__main__':
    instance.run(host='192.168.11.10', port='8890', debug=True, )
