import requests
from dataclasses import dataclass
from molgan.constants import MOLGAN_API_SAMPLE_MOL, MOLGAN_API_PREDICT, DISEASES

@dataclass
class Disease:
    name: str
    prediction: int

def get_generate_smiles():
    smiles = requests.get(MOLGAN_API_SAMPLE_MOL).json().get('SMILES')
    return smiles

def get_disease_prediction(smiles):
    return dict(requests.get(MOLGAN_API_PREDICT + smiles).json())

def prediction_to_disease_table(prediction):
    return [Disease(name=disease, prediction=pred) for disease, pred in zip(DISEASES, prediction.values())]