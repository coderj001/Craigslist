import requests

from bs4 import BeautifulSoup
from core.forms import SearchForm
from django.shortcuts import render


def home(request):
    return render(request,'core/home.html',context={})

def new_search(request):
    if request.method == 'POST':
        forms=SearchForm(request.POST)
        if forms.is_valid():
            stuff_to_frontend=forms.cleaned_data['search']
        return render(request,'core/search.html',context={'forms':forms,'content_data':stuff_to_frontend})
    else:
        forms=SearchForm()
        # BUG: Debug forms widgets need to change
        # import pdb; import pdb; pdb.set_trace()
        return render(request,'core/search.html',context={'forms':forms})
