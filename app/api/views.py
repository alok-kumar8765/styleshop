from django.db.models.query import QuerySet
from app.models import Customer,Product,Cart,OrederPlaced
from app.api.serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
import requests
from rest_framework.generics import RetrieveAPIView
from rest_framework import serializers

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    authentication_classes=[TokenAuthentication,SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
#class CustomerView(APIView):
    
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    
    #def get(self, request, format=None):
        #content = {
            #'user': str(request.user),  # `django.contrib.auth.User` instance.
            #'auth': str(request.auth),  # None
        #}
        #return Response(content)
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer

    def get_object(self):
        return self.request.user
'''
for gen token type in terminal : python manage.py drf_create_token simon

'''