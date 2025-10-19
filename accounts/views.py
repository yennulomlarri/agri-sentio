# from django.http import JsonResponse
# from django.views import View

# class RegisterView(View):
#     def get(self, request):
#         return JsonResponse({"message": "Register endpoint placeholder"})

# class LoginView(View):
#     def get(self, request):
#         return JsonResponse({"message": "Login endpoint placeholder"})

# class ProfileView(View):
#     def get(self, request):
#         return JsonResponse({"message": "Profile endpoint placeholder"})

from django.http import JsonResponse
from django.views import View

class RegisterView(View):
    def get(self, request):
        return JsonResponse({"message": "Register endpoint placeholder"})

class LoginView(View):
    def get(self, request):
        return JsonResponse({"message": "Login endpoint placeholder"})

class ProfileView(View):
    def get(self, request):
        return JsonResponse({"message": "Profile endpoint placeholder"})
    

   