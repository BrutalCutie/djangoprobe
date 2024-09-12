from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'catalog/success.html')

    return render(request, 'catalog/contacts.html')

