"""
Copyright (c) Meta Platforms, Inc. and affiliates.
All rights reserved.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import os
import tqdm
import urllib.request
import zipfile


def download_file(url, filename):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        with open(filename, 'wb') as file:
            file.write(data)


def unzip_file(zip_path, extract_to):
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


for i in tqdm.tqdm(range(1, 108), desc="download 107 speakers of EARS dataset"):
    url = f"https://github.com/facebookresearch/ears_dataset/releases/download/dataset/p{i:03d}.zip"
    file = f"p{i:03d}.zip"
    download_file(url, file)
    unzip_file(file, ".")
    os.remove(file)

