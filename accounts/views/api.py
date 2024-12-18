from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class UserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'username': request.user.username,  
            'email': request.user.email,
            'phone' : request.user.phone,
            'is_active': request.user.is_active,
            'is_admin': request.user.is_admin,
        }

        return Response(content)
