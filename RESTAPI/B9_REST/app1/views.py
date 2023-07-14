from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# def get_student(request, id):
#     stud_obj = Student.objects.get(id=id)   # complex data
#     # print(stud_obj.__dict__)           # {'_state': <django.db.models.base.ModelState object at 0x000001E102463950>, 'id': 1, 'name': 'AAA', 'age': 22, 'address': 'Pune', 'marks': 78}
#     stud_obj.__dict__.pop("_state")
#     # print(stud_obj.__dict__)             # {'id': 1, 'name': 'AAA', 'age': 22, 'address': 'Pune', 'marks': 78}
#     data = json.dumps(stud_obj.__dict__)
#     return HttpResponse(data)

def get_student(request, id):
    stud_obj = Student.objects.get(id=id)
    python_data = StudentSerializer(stud_obj)  # python dict
    # print(python_data.data)
    bytes_data = JSONRenderer().render(python_data.data)  # bytes data -- json.dumps
    print(bytes_data)
    return HttpResponse(bytes_data, content_type="application/json")
    # return HttpResponse("Success")


def get_all_students(request):
    all_studs = Student.objects.all() # complex data -- queryset
    python_data = StudentSerializer(all_studs, many=True)  # python dict
    bytes_data = JSONRenderer().render(python_data.data)
    return HttpResponse(bytes_data, content_type="application/json")

import io

@csrf_exempt
def create_students(request):
    if request.method == "POST":
        # print(request.body)
        # print(request.user)
        # print(dir(request))
        # print(request.build_absolute_uri())
        bytes_data = request.body   # bytes data
        my_json = bytes_data.decode('utf8').replace('"','"')  # bytes to json
        # print(type(my_json))
        py_dict = json.loads(my_json)
        ser = StudentSerializer(data=py_dict)
        if ser.is_valid():
            data = ser.save()
            print(data.__dict__)
            data.__dict__.pop("_state")
            json_msg = json.dumps(data.__dict__)
            # success_msg = {"msg": "Data inserted successfully.."}
            # json_msg = json.dumps(success_msg)
            return HttpResponse(json_msg, status=status.HTTP_201_CREATED, content_type="application/json")

        # return HttpResponse("POST Request", status=status.HTTP_201_CREATED, content_type="application/json")
    else:
        error_msg = {"msg": "Only post method is allowed"}
        json_data = json.dumps(error_msg)
        return HttpResponse(json_data, content_type="application/json",status=status.HTTP_405_METHOD_NOT_ALLOWED)

