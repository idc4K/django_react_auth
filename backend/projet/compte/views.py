# from django.shortcuts import render
# from django.http import HttpResponse

# from django.contrib.auth.models import User
# from rest_framework.views import APIView
# from rest_framework import permissions
# from django.contrib import auth
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserCreateSerializer
# from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
# from django.utils.decorators import method_decorator
# from .forms import formail

# @method_decorator(csrf_protect, name='dispatch')
# class HomeView(APIView):
#     permission_classes = (permissions.AllowAny, )
#     def all(self, request,format=None):
#         api_urls = {
#             'create_user':'/register/',
            
#             }
#         return Response(api_urls)
	  
# class CheckAuthenticatedView(APIView):
#     def get(self, request, format=None):
#         user = self.request.user

#         try:
#             isAuthenticated = user.is_authenticated

#             if isAuthenticated:
#                 return Response({ 'isAuthenticated': 'success' })
#             else:
#                 return Response({ 'isAuthenticated': 'error' })
#         except:
#             return Response({ 'error': 'Something went wrong when checking authentication status' })

# @method_decorator(csrf_protect, name='dispatch')
# class SignupView(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def post(self, request, format=None):

#         if request.method == 'POST':
#             email = request.POST.get('email')
#             first_name = request.POST.get('first_name')
#             password1 = request.POST.get('password1')
#             password2 = request.POST.get('password2')
            
#             form = formail(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.is_active = False
#                 user.save()
#                 current_site = get_current_site(request)
#                 subject = 'merci pour votre inscription'
#                 message = render_to_string('Mail/compte/envoyer.html', {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                 })
#                 email_from = settings.EMAIL_HOST_USER
#                 user.email_user(subject, message,email_from)

#                 return Response({ 'success': 'User crée avec succès' })

#             elif User.objects.filter(first_name=first_name).exists():
                
#                 return Response({ 'error': 'ce nom est déjà pris' })

#             elif User.objects.filter(email=email).exists():
#                 return Response({ 'error': 'ce mail existe déjà' })
                

#             elif password1 != password2:
#                 return Response({ 'error': 'mot de passe trop court' })



# @method_decorator(csrf_protect, name='dispatch')
# class ActivateView(APIView):
#     def activate(self,request, uidb64, token):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None

#         if user is not None and account_activation_token.check_token(user, token):
#             user.is_active = True
#             user.profile.email_confirmed = True
#             user.save()
#             login(request, user)
#             return Response({'succes':"compte activé"})
#         else:
#             return Response({'error': "erreur d'activation"})
# # @method_decorator(csrf_protect, name='dispatch')
# # class LoginView(APIView):
# #     permission_classes = (permissions.AllowAny, )

# #     def post(self, request, format=None):
# #         data = self.request.data

# #         username = data['username']
# #         password = data['password']

# #         try:
# #             user = auth.authenticate(username=username, password=password)

# #             if user is not None:
# #                 auth.login(request, user)
# #                 return Response({ 'success': 'User authenticated' })
# #             else:
# #                 return Response({ 'error': 'Error Authenticating' })
# #         except:
# #             return Response({ 'error': 'Something went wrong when logging in' })

# # class LogoutView(APIView):
# #     def post(self, request, format=None):
# #         try:
# #             auth.logout(request)
# #             return Response({ 'success': 'Loggout Out' })
# #         except:
# #             return Response({ 'error': 'Something went wrong when logging out' })

# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRFToken(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def get(self, request, format=None):
#         return Response({ 'success': 'CSRF cookie set' })

# # class DeleteAccountView(APIView):
# #     def delete(self, request, format=None):
# #         user = self.request.user

# #         try:
# #             User.objects.filter(id=user.id).delete()

# #             return Response({ 'success': 'User deleted successfully' })
# #         except:
# #             return Response({ 'error': 'Something went wrong when trying to delete user' })
# # Create your views here.
