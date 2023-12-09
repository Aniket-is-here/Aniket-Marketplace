from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from item.models import Item
from django.contrib.auth import logout

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'account/index.html', {
        'items': items
    })


@login_required
def logout_view(request):
    logout(request)

    return redirect('core:index')
