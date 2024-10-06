# study mart:
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator #amra akn a class based use korci tai ai line ta deya ta drk 
from django.views import View #amra akn a class based use korci


#amra akn a class based use korci
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data  = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer =StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application.json')
        
        student = Student.objects.all()# akn a amra (many =True) aita use korar karon amara (info = Student.objects.all() ai line a (Student) model a onek data ace tai amra many= true use korci nah korle error asbe
        serializer = StudentSerializer(student, many =True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application.json')
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        # json_data to stame:
        stream = io.BytesIO(json_data) 
        # strame to python data:
        python_data = JSONParser().parse(stream)
        # python to complex_data/serializer
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(response_msg)
            return HttpResponse(json_data, content_type='application.json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type= 'application.json')
    

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id  =python_data.get('id')
        student = Student.objects.get(id =id)
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            r = {'msg: Data Updated'}
            json_data = JSONRenderer().render(r)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id = id)
        student.delete()
        r = {'msg: Data Deleted'}
        json_data = JSONRenderer().render(r)
        return HttpResponse(json_data,content_type = 'application/json')

        