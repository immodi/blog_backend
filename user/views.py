from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .forms import *


class RegisterUser(APIView):
    def post(self, request):
        print(request.POST)
        try: 
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email']
                )
                if form.cleaned_data.get('is_staff', False): 
                    user.is_staff = True
                user.set_password(form.cleaned_data['password'])
                user.save()
                return Response(form.cleaned_data)
            else:
                raise Exception(form.errors.get_json_data())
        except Exception as e:
            return Response({"error": str(e)})
    

class GetUserNameWithToken(APIView):
    def post(self, request):
        try: 
            token = request.POST.get("token")
            user_id = Token.objects.get(key=token).user_id
            user = User.objects.get(id=user_id)
            
            return Response({
                "username": user.username,
            })

        except Exception as e:
            return Response({"error": e})


# class LogoutUser(APIView):
#     def get(self, request):
#         logout(request)
#         return Response({
#             "status": "logged out successfuly :/"
#         })


class GetUserByUserName(APIView):    
    def post(self, request):
        try: 
            username = request.POST["username"]
            user = User.objects.get(username=username)
            data = {
                "userName": user.get_username(),
                "isAdmin": user.is_staff,
            }
        except Exception: data = {
            'error': "Invalid Username"
        }
        return Response(data)
