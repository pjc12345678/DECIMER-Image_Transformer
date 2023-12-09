import os
print(os.getcwd())
from decimer import predict_SMILES

print("OK")
image_path = "1234_bnw_0.png"
SMILES = predict_SMILES(image_path)
print(SMILES)