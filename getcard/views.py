from django.shortcuts import render,HttpResponse
from getcard.models import form
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        birth = request.POST['birth']
        frm = request.POST['frm']
        to = request.POST['to']
        special_number = request.POST['special_number']
        contact = form(name=name,  phone=phone,email=email,birth=birth,frm=frm,to=to,special_number=special_number)
        contact.save()
    return render(request, './html/index.html')

def card(request):
    all = form.objects.all()
    print(all)
    return render(request, './html/card.html',{'all':all[1]})