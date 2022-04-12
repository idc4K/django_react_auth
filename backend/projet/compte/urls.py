from django.urls import path,include
from .views import CheckAuthenticatedView,SignupView,GetCSRFToken,ActivateView,HomeView

urlpatterns = [
   
    # path('',HomeView.as_view()),
    # path('authenticated', CheckAuthenticatedView.as_view()),
    # path('register', SignupView.as_view()),
    # path('activate/<uidb64>/<token>/', ActivateView.as_view()),
    # path('login', LoginView.as_view()),
    # path('logout', LogoutView.as_view()),
    # path('delete', DeleteAccountView.as_view()),
    # path('csrf_cookie', GetCSRFToken.as_view())
]