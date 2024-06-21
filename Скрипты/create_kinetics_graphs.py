import os
from tqdm import tqdm

from MDR_base import process

for root, dirs, files in os.walk("../Измерения/с комплекса/со спектрометра", topdown=False):
    for name in tqdm(files):
        file = os.path.join(root, name)
        if file.endswith(".png"): continue
        if file.endswith(".mdrk"):
            process(file)
