from django.shortcuts import render
import execjs



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

    content = {
        'data': v,
    }
    return render(request, 'index.html', content)
# Create your views here.



