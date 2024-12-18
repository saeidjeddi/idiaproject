from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class JsonResponse404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return JsonResponse({
                'error': 'خطا 404',
                'message': 'درخواست شما اشتباه هست '
            }, status=404)
        return response