from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
path('home/',views.HomePageView.as_view(),name="home"),
path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
path('register/', views.UserCreate.as_view(),name="register"),
path('Aadhar/', views.get_aadhar),
path('AddAadhar/', views.add_aadhar),
path('UpdateAadhar/<int:aadhar_number>', views.update_aadhar),
path('DeleteAadhar/<int:aadhar_number>', views.delete_aadhar)
]