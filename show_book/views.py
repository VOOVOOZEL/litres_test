import requests

from django.shortcuts import render
from .forms import NameForm


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            payload = {"email": request.POST.get("your_name"), "password": request.POST.get("your_pass")}
            r = requests.post('https://mybook.ru/api/auth/', data=payload)
            if r.ok:
                cookies = r.cookies.get_dict()
                books = requests.get('https://mybook.ru/api/bookuserlist/', cookies=cookies)
                data = books.json()
                count = len(data['objects'])
                return render(request, "index.html", {'objects': data['objects'], 'count': count})
            else:
                return render(request, 'login.html', {'form': form, 'res': request})
    else:
        form = NameForm()
    return render(request, 'login.html', {'form': form})
