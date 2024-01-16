from django.urls import path,include
from . import views
from rest_framework import routers

# from .views import get_animals
router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'adopters', views.AdopterViewSet)




urlpatterns = [
    # path("animals/",views.get_animals, name ="animals"),
    # path("animals/<int:animal_id>/",views.get_animal_id, name ="animal"),
    path('', include(router.urls)),
    # path("adopters/", views.get_adopter, name="adopters"),
    # path("adopters/<str:adopter_ssn>/", views.get_adopter_ssn, name="adopter")
]


urlpatterns += router.urls
