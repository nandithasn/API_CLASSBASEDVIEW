from django.shortcuts import render

from rest_framework.views import APIView
from app.serializers import *
from app.models import *
from rest_framework.response import Response

# Create your views here.


class ProductNandu(APIView):
    

    def get(self,request,pk):
        DO=Product.objects.all()
        CO=ProductMS(DO,many=True)
        return Response(CO.data)
    

    def post(self,request,pk):
        rdo=request.data # request is 
        cdo=ProductMS(data=rdo)# it is used for convering JSON DATA TO PYTHON
        if cdo.is_valid():
            cdo.save()
            return Response({'msg':'data is inserted successfully'})
        else:
            return Response({'msg':'data is not inserted'})
        
    
    def put(self,request,pk):
        rdo=request.data
        instance=Product.objects.get(pk=pk)# here we are creating instance
        cdo=ProductMS(instance,data=rdo)
        if cdo.is_valid():
            cdo.save()
            return Response({'updated':'success'})
        else:
            return Response({'failed':'failed'})
        

    def patch(self,request,pk):
        rdo=request.data  #
        instance=Product.objects.get(pk=pk)
        cdo=ProductMS(instance,data=rdo,partial=True)
        if cdo.is_valid():
            cdo.save()
            return Response({'Parial Update':'success'})
        else:
            return Response({'no partial Update':'failed'})
        

    def delete(self,request,pk):
        instance=Product.objects.get(pk=pk).delete()
        return Response({'delete':'success'})

