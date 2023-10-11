from django.shortcuts import render, redirect
from django.views.generic import View
from molgan.utils import get_generate_smiles, get_disease_prediction, prediction_to_disease_table
from django.contrib import messages

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        smiles = request.GET.get('smiles')
        if not smiles:
            smiles = ''
        return render(request, 'molgan/index.html', {'smiles': smiles})
    
    def post(self, request, *args, **kwargs):
        smiles = request.POST.get('smiles')
        return redirect('predict', smiles=smiles)
    
async def generate_smiles(request):
    smiles = await get_generate_smiles()
    return redirect('/?smiles=' + smiles)

class PredictView(View):
    async def get(self, request, smiles='', *args, **kwargs):
        disease_prediction = await get_disease_prediction(smiles)
        if disease_prediction.get('error'):
            messages.error(request, disease_prediction.get('error'))
            return redirect('index')
        disease_table = prediction_to_disease_table(disease_prediction)
        return render(request, 'molgan/predict.html', {'smiles': smiles, 'disease_table': disease_table})
    
class PredictListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'molgan/predict_list.html')
    
    def post(self, request, *args, **kwargs):
        smiles = request.POST.get('smiles')
        print(smiles)
        return redirect('index')

def handler404(request, *args, **kwargs):
    return render(request, 'molgan/404.html')