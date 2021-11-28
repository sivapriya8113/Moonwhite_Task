from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import customerserializer,addressserializer,requestserilaizer
from .models import customerdetails,Address



@api_view(['Post'])
def InsertCustomer(request):
    serializer = requestserilaizer(data=request.data)
    #import pdb;pdb.set_trace()
    if serializer.is_valid():

        a = customerdetails(firstname=serializer.data.get('firstname'), lastname=serializer.data.get('lastname'), email=serializer.data.get('email'),mobileno=serializer.data.get('mobileno'))
        a.save()
        b = Address(customer_id=a, addr_line1=serializer.data.get('addr_line1'),
                    addr_line2=serializer.data.get('addr_line2'), city=serializer.data.get('city'),state=serializer.data.get('state'),pincode=serializer.data.get('pincode'),
                    )
        b.save()
        #serializer.save()
    return Response(serializer.data)

''''
@api_view(['Get'])
def showall(request):
    customer = customerdetails.objects.all()
    serializer = customerserializer(customer, many=True)
    return Response(serializer.data)
    
    '''
