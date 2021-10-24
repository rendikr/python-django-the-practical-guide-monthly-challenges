from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number), # /challenges/1
    path("<str:month>", views.month_challenge, name="month-challenge") # /challenges/january
]
