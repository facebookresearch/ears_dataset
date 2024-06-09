"""
Copyright (c) Meta Platforms, Inc. and affiliates.
All rights reserved.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import os
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


print("downloading blind testset (1.4GB)...")
url = "https://github.com/facebookresearch/ears_dataset/releases/download/blind_testset/blind_testset.zip"
file = f"blind_testset.zip"
download_file(url, file)
unzip_file(file, "blind_testset")
os.remove(file)

