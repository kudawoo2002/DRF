from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from students.models import Student
from employees.models import Employee
from products.models import Product
from asserts.models import Assert
from .serializers import StudentSerializer, EmployeeSerializer, AssertSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer

# Create your views here.

@api_view(["GET", "POST"])
def studentsView(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(["GET",'PUT','DELETE'])
def studentDetailView(request, pk):
    
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "DELETE":
            
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    


class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    


class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
           raise Http404()
        
    def get(self, request, pk):
        employeeDetail = self.get_object(pk=pk)
        serializer = EmployeeSerializer(employeeDetail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employeeDetail = self.get_object(pk)
        seriliazer = EmployeeSerializer(employeeDetail, data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(seriliazer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        employeeDetail = self.get_object(pk)
        employeeDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class Products(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class ProductDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    

'''
class Asserts(generics.ListCreateAPIView):
    queryset = Assert.objects.all()
    serializer_class = AssertSerializer



class AssertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assert.objects.all()
    serializer_class = AssertSerializer
    lookup_field = "pk"
'''

# ViewSet class base

# class AssertsViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Assert.objects.all()
#         serializer = AssertSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = AssertSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     def retrieve(self, request, pk=None):
#         assert_obj = get_object_or_404(Assert, pk=pk)
#         serializer = AssertSerializer(assert_obj)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         assert_obj = get_object_or_404(Assert, pk=pk)
#         serializer = AssertSerializer(assert_obj,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#     def destroy(self, request, pk=None):
#         assert_obj = get_object_or_404(Assert, pk=pk)
#         assert_obj.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)


class AssertsViewset(viewsets.ModelViewSet):
    queryset = Assert.objects.all()
    serializer_class = AssertSerializer


class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"