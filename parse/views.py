from django.shortcuts import render

def upload(request):

    v = request.GET['data']
    content = {
        'data': v,
    }
    return render(request, 'index.html', content)


# Create your views here.



