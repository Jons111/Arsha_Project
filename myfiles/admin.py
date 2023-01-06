from django.contrib import admin
from myfiles.models import Portfolio,Tur,Murojaat
# Register your models here.

class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Tur,AdminTur)

class AdminPort(admin.ModelAdmin):
    list_display = ['id','nomi','date','tur','rasm1','vaqt']

admin.site.register(Portfolio,AdminPort)


class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id','name','gmail','title','text','date']

admin.site.register(Murojaat,AdminMurojaat)