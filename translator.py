from transformers import MarianTokenizer, MarianMTModel
from transformers import FSMTForConditionalGeneration, FSMTTokenizer
import os
from typing import List


class Translator():
    def __init__(self, model_dir):
        self.models = {}
        self.models_dir = model_dir
        self.load_model('de', 'en')

    def get_supported_langs(self):
        routes = [x.split('-')[-2:] for x in os.listdir(self.models_dir)]
        return routes

    def load_model(self, source, target):
        route = f'{source}-{target}'
        path = os.path.join(self.models_dir, f'wmt19-{route}-6-6-base')
        model = FSMTForConditionalGeneration.from_pretrained(path)
        tok = FSMTTokenizer.from_pretrained(path)
        self.models[route] = (model, tok)

    def translate(self, source, target, text):

        route = f'{source}-{target}'
        model, tokenizer = self.models[route]

        input_ids = tokenizer.encode(text, return_tensors="pt")
        outputs = model.generate(input_ids)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
