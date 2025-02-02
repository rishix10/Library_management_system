from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('manage books',views.manage),
    path('student',views.students),
    path('manage1',views.book),
    path('stu',views.stu),
    path('insert',views.ins),
    path('stuins',views.stuins),
    path('issert',views.issert),
    path('issues',views.issues),
    path('issuing',views.issuing),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    path('delis/<int:id>',views.delis),
    path('delib/<int:id>',views.delib),
    path('delis/<int:id>',views.delis),
    path('logon',views.logon),
    path('login',views.log),
]