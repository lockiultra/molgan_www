from django.urls import path
from molgan.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('generate_smiles', generate_smiles, name='generate_smiles'),
    path('predict/<smiles>', PredictView.as_view(), name='predict'),
    path('predict_list', PredictListView.as_view(), name='predict_list'),
]