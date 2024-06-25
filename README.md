# EARS Dataset

We release the **E**xpressive **A**nechoic **R**ecordings of **S**peech (EARS) dataset.

If you use the dataset or any derivative of it, please cite our [Paper](https://arxiv.org/abs/2406.06185)

```
@inproceedings{richter2024ears,
  title={{EARS}: An Anechoic Fullband Speech Dataset Benchmarked for Speech Enhancement and Dereverberation},
  author={Richter, Julius and Wu, Yi-Chiao and Krenn, Steven and Welker, Simon and Lay, Bunlong and Watanabe, Shinjii and Richard, Alexander and Gerkmann, Timo},
  booktitle={Interspeech},
  year={2024}
}
```

For audio samples or scripts to generate the speech enhancement benchmarks, please visit the [project page](https://sp-uhh.github.io/ears_dataset/).

## Highlights
* **100 h** of speech data from **107 speakers**
* high-quality recordings at **48 kHz** in an anechoic chamber
* **high speaker diversity** with speakers from different ethnicities and age range from 18 to 75 years
* **full dynamic range** of human speech, ranging from whispering to yelling
* 18 minutes of **freeform monologues** per speaker
* sentence reading in **7 different reading styles** (regular, loud, whisper, high pitch, low pitch, fast, slow)
* emotional reading and freeform tasks covering **22 different emotions** for each speaker

## Download EARS Dataset

### using bash
```
for X in $(seq -w 001 107); do
  curl -L https://github.com/facebookresearch/ears_dataset/releases/download/dataset/p${X}.zip -o p${X}.zip
  unzip p${X}.zip
  rm p${X}.zip
done
```

### using python
run the [EARS download script](https://github.com/facebookresearch/ears_dataset/blob/main/download_ears.py)
```
python download_ears.py
```

## Download Blind Testset with Noisy Speech

### using bash
```
curl -L https://github.com/facebookresearch/ears_dataset/releases/download/blind_testset/blind_testset.zip -o blind_testset.zip
mkdir blind_testset
unzip blind_testset.zip -d blind_testset
rm blind_testset.zip
```

### using python
run the [blind testset download script](https://github.com/facebookresearch/ears_dataset/blob/main/download_blind_testset.py)
```
python download_blind_testset.py
```

## Statistics and Transcripts
The speaker statistics (age, ethnicity, gender, weight, height, native language) for the 107 speakers are collected in [speaker_statistics.json](https://github.com/facebookresearch/ears_dataset/blob/main/speaker_statistics.json).

Transcripts of the reading portions of the dataset are available in [transcripts.json](https://github.com/facebookresearch/ears_dataset/blob/main/transcripts.json).

# License
The code and dataset are released under [CC-NC 4.0 International license](https://github.com/facebookresearch/ears_dataset/blob/main/LICENSE).
