import json

from django.shortcuts import render
import execjs
from django.http import HttpResponse



def get_js():
    # f = open("D:/WorkSpace/MyWorkSpace/jsdemo/js/des_rsa.js",'r',encoding='UTF-8')
    f = open("static/decode.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


def upload(request):
    jsstr = get_js()
    ctx = execjs.compile(jsstr)
    v = ctx.call('decodeMessage', request.GET['data'])

    print(v)
    return HttpResponse(json.dumps(v), content_type="application/json")
    # return render(request, 'index.html', content)




