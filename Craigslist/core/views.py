from core.forms import SearchForm
from django.shortcuts import render


def home(request):
    return render(request,'core/home.html',context={})

def new_search(request):
    forms=SearchForm()
    # BUG: Debug forms widgets need to change
    # import pdb; import pdb; pdb.set_trace()
    return render(request,'core/search.html',context={'forms':forms})
