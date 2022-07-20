from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home(request):
    
    client_list = Client.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(client_list, 10)

    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
        'clients':clients
    }    
    return render(request, 'clientspage.html', context)    

