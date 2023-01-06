import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import Tur,Portfolio,Murojaat
# Create your views here.

def home(malumot):
    if 'malumot' in malumot.POST:
        matn = malumot.POST.get('malumot')
        print(matn)
        soz = str(matn).strip()
        print(soz)
        qidirish = Q(nomi__icontains  = soz)| Q(cleant_nomi__startswith=soz)| Q(date__icontains=soz)| Q(link__icontains=soz)|   Q(malumot__icontains = soz)|   Q(tur__id__icontains = soz)
        ishlarimiz = Portfolio.objects.filter(qidirish)
        return render(malumot, 'index.html', {'works': ishlarimiz})

    elif malumot.method =='POST':
        ismi = malumot.POST.get('ismii')
        gmaili = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        matn = malumot.POST.get('message')
        vaqti = datetime.datetime.now()
        Murojaat(name=ismi,gmail=gmaili,title=subject,text=matn,date=vaqti).save()
        ishlarimiz = Portfolio.objects.all()
        return render(malumot,'index.html',{'works':ishlarimiz})
    else:
        ishlarimiz = Portfolio.objects.all()
        return render(malumot, 'index.html', {'works': ishlarimiz})

def inner(malumot):
    return render(malumot,'inner_page.html')

def portfolio(malumot,id):
    ishlarimiz = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':ishlarimiz})