from django.shortcuts import render
# from .Mlalgo import naive,knn,logistict,rf,decisionTree,svm
from .Mlalgo import logistict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictSerializer


# Create your views here.

@api_view(['POST'])
def predict(request):
    if 'text' in request.data:
        text = request.data['text']
        print(text)
        result = logistict(text)
        serializer = PredictSerializer({'result': result})
        return Response(serializer.data)
    else:
            response = {'message': 'You need to provide Text'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # data = request.data
    # return Response({'message':'Error'})


