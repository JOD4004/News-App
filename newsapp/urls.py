from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('business',views.business,name="business"),
    path('entertainment',views.entertainment,name="entertainment"),
    path('general',views.general,name="general"),
    path('health',views.health,name="health"),
    path('science',views.science,name="science"),
    path('sports',views.sports,name="sports"),
    path('technology',views.technology,name="technology"),
]