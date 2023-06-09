from django.shortcuts import render
from django.urls import reverse
from .models import crud
from django.http import HttpResponseRedirect
from .forms import CrudForm

# Create your views here.
def index(request):
    data = crud.objects.all()
    return render(request,'index.html',{"datas":data})

def save_data(request):
        if request.method == 'POST':
            sl_no = request.POST.get('slno')
            item_name = request.POST.get('itemname')
            description = request.POST.get('description')
            cr = crud(sl_no=sl_no,item_name=item_name,description=description)
            cr.save()
        return HttpResponseRedirect(reverse('index'))


def update(request,data_id):
    cr = crud.objects.get(id=data_id)
    cr_form = CrudForm()
    if cr_form.is_valid():
        cr_form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'update.html', {'cr_form': cr_form, 'crud': cr})


def delete(request,data_id):
    if request.method == 'POST':
        cr = crud.objects.get(id=data_id)
        cr.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'delete.html', {'crud': crud})
