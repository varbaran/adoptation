from django.shortcuts import render, get_object_or_404
from .models import Animal, Adopter, Dog, Cat
from .serializers import AnimalSerializer, AdopterSerializer
from django.http import JsonResponse
from rest_framework import permissions, viewsets, mixins


# Create your views here.
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.select_subclasses()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)


class AdopterViewSet(viewsets.ModelViewSet):
    queryset = Adopter.objects.all()
    lookup_field = 'ssn'
    serializer_class = AdopterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    #
    # def list(self, request, *args, **kwargs):
    #     print(dict(AdopterSerializer))
    #     return super().list(request, *args, **kwargs)



# def get_animals(request):
#     animals = Animal.objects.select_subclasses()                  # for string
#     only_available = request.GET.get("only_available","false").lower()
#     # this == up
#     # try:
#     #     only_available = request.GET["only_available"]
#     # except KeyError:
#     #     only_available = "false"
#     # only_available.lower()
#     results = []
#     for animal in animals:
#         result = {
#             "id" : animal.id,
#             "name" : animal.name,
#             "age" : animal.age,
#             "type" : animal.__class__.__name__,
#             "adopted" : True if animal.adopter is not None else False
#         }
#         results.append(result)
#
#     if only_available == "true":
#         results = [x for x in results if x["adopted"] is False]
#         for result in results:
#             del result["adopted"]
#         # animals = animals.filter(adopter__isnull=True)
#         return JsonResponse({
#             "animals": results
#         })
#     else:
#         return JsonResponse({
#             "animals": results
#         })
#
#

# def get_animal_id(request, animal_id):
#     try:
#         animal = Animal.objects.get_subclass(id = animal_id)
#     except Animal.DoesNotExist:
#         return JsonResponse({"eror": "DoesNotExist"}, status= 404)
#     return JsonResponse({
#         "animal": {
#             "id": animal.id,
#             "name": animal.name,
#             "age": animal.age,
#             "type": animal.__class__.__name__,
#             "adopted": True if animal.adopter is not None else False,
#         }
#     })

# def get_adopter(request):
#     adopters = Adopter.objects.all()
#     return JsonResponse({
#         "adopters": list(adopters.values())
#     })
#
# def get_adopter_ssn(request, adopter_ssn):
#     adopter = get_object_or_404(Adopter, ssn=adopter_ssn)
#     return JsonResponse({
#         "name": adopter.name
#     })
