from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        return render(request, 'home.html',{ 'new_item_text': new_item_text})
    else:
        return render(request, 'home.html',{ 'new_item_text': ''})
        