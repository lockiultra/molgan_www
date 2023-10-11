import requests
import aiohttp
from dataclasses import dataclass
from molgan.constants import MOLGAN_API_SAMPLE_MOL, MOLGAN_API_PREDICT, DISEASES

@dataclass
class Disease:
    name: str
    prediction: int

async def get_generate_smiles():
    async with aiohttp.ClientSession() as session:
        async with session.get(MOLGAN_API_SAMPLE_MOL) as response:
            smiles = await response.json()
            return smiles.get('SMILES')

async def get_disease_prediction(smiles):
    async with aiohttp.ClientSession() as session:
        async with session.get(MOLGAN_API_PREDICT + smiles) as response:
            return await response.json()

def prediction_to_disease_table(prediction):
    return [Disease(name=disease, prediction=pred) for disease, pred in zip(DISEASES, prediction.values())]