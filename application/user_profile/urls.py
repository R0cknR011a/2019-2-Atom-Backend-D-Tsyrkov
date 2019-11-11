from user_profile.views import timon, pumba
from django.urls import path

urlpatterns = [
    path('timon/', timon, name='timon'),
    path('pumba/', pumba, name='pumba'),
]
