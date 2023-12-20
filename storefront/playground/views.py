
# import requests
# from rest_framework.views import APIView 
# from django.shortcuts import render
# import logging

# logger = logging.getLogger(__name__)


# class HelloView(APIView):
#     def get(self, request):
#         try:
#             logger.info('Calling httpbin')
#             response = requests.get('https://httpbin.org/delay/2')
#             logger.info('Received the response')
#             data = response.json
#         except requests.ConnectionError:
#             logger.critical('httpbin is offline')
#         return render(request, 'hello.html', {'name': 'Mosh'})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
import requests
from rest_framework.views import APIView 
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')  # Corrected the typo in URL
            data = response.json()
            # Process your data and return an appropriate response
            return HttpResponse(data)  # Modify this line as needed
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
            return render(request, 'hello.html', {'name': 'Mosh'})
