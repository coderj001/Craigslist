import asyncio
from core.forms import SearchForm
from core.models import Search
from django.shortcuts import render

from .utils import searching


async def home(request):
    return render(request, 'core/home.html', context={})


async def new_search(request):
    if request.method == 'POST':
        forms = SearchForm(request.POST)
        if forms.is_valid():
            stuff_to_frontend = await searching(forms.cleaned_data['search'])
            # TODO:  <19-01-21, coderj001>
            # django sync_to_async support need to save query
            # forms.save()
        return render(
            request,
            'core/search.html',
            context={
                'forms': forms,
                'content_data': stuff_to_frontend
            }
        )
    else:
        forms = SearchForm()
        return render(request, 'core/search.html', context={'forms': forms})
