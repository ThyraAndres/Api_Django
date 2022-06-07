from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
import json
# Create la as viws donde podremos interactuar con la base de datos company

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company =  companies[0]
                datos = {'message': "EXITO", 'companies': company}
            else:
                datos = {'message': "compañia no encontrada  ... "}
            return JsonResponse(datos)

        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message': "EXITO", 'companies': companies}
            else:
                datos = {'message': "COMPAÑIA NO ENCONTRADA ... "}
            return JsonResponse(datos)
    def post(self, request):

        jd =json.loads(request.body)
        Company.objects.create(nombre=jd['nombre'], website=jd['website'], foundation=jd['foundation'])
        datos = {'message': "EXITO"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd =json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company= Company.objects.get(id=id)    
            company.nombre = jd['nombre']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': "Actualizacion hecha"}
        else:
            datos = {'message': "Compañia no encontrada ... "}
        return JsonResponse(datos)

    def delete(self, request,id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()    #pregunta si el id existe y si es un si se aplica el delete
            datos = {'message': "EXITO AL ELIMINAR"}
        else:
            datos = {'message': "COMPAÑIA NO ENCONTRADA ... "}
        return JsonResponse(datos)

