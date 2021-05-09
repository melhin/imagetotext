import os
import argparse
import urllib
from urllib.request import urlretrieve


HUGGINGFACE_S3_BASE_URL="https://s3.amazonaws.com/models.huggingface.co/bert/allenai"
FILENAMES = ["config.json", "pytorch_model.bin", "tokenizer_config.json", "merges.txt", "tokenizer_config.json", "vocab-src.json", "vocab-tgt.json"]
MODEL_PATH = "data"

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, help='source language code')
parser.add_argument('--target', type=str, help='target language code')

def download_language_model(source,target):
    model = f"wmt19-{source}-{target}-6-6-base"
    print(">>>Downloading data for %s to %s model..." % (source, target))
    os.makedirs(os.path.join("data",model),exist_ok=True)
    for f in FILENAMES:
        try:
            print(os.path.join(HUGGINGFACE_S3_BASE_URL,model,f))
            urlretrieve(os.path.join(HUGGINGFACE_S3_BASE_URL,model,f),
                                        os.path.join(MODEL_PATH,model,f))
            print("Download complete!")
        except urllib.error.HTTPError:
            print("Error retrieving model from url. Please confirm model exists.")

if __name__ == "__main__":
    args = parser.parse_args()
    download_language_model(args.source, args.target)
