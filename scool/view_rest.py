from rest_framework.views import APIView

from rest_framework.response import Response
from .models import Course, Person
from django.forms.models import model_to_dict
from rest_framework import generics
from .serializers import CourseSerializer, PersonSerializer

# v1 ----------    
class CourseAPIView(APIView):
    # def get(self, reques):
    #     return Response({'name':'Python','num':'11'})
    
    # def post(self, request):
        # return Response({'name':'JS','num':'22'})


    def get(self, r, **kwargs):        
        courses = Course.objects.all().values()
        return Response({'courses':list(courses)})

    def post(self, r):
        course = Course.objects.create(
            name = r.data['name'],
            course_num = r.data['num'],
            description = r.data['descr']
        )

        return Response(
            {'couse':model_to_dict(course)}
        )

    def put(self, r, *args, **kwargs):        
        pk = kwargs.get("pk", None)        
        if not pk:
            return Response({"error": "Method PUT not allowed"})
 
        try:
            course = Course.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        course.name = r.data['name']
        course.course_num = r.data['num']
        course.description = r.data['descr']        
        course.save() 
        return Response({'couse':model_to_dict(course)}) 



# v2 ------------------------


# class CourseAPIView2(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# AllowAny – полный доступ;
# IsAuthenticated – только для авторизованных пользователей;
# IsAdminUser – только для администраторов;
# IsAuthenticatedOrReadOnly – только для авторизованных или всем, но для чтения.

from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly ) 
# свои классы доступа
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class CourseAPIView2(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseApiUpdate(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

class CourseApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,IsAuthenticatedOrReadOnly)



# v3 -----------------
from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
