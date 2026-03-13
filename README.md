# Semi-supervised anomaly traffic detection via multi-frequency reconstruction

---

## 🧩 Overview
**We are the first to reveal that traffic images contain rich high-frequency information and exhibit irregular pixel distributions. To address this issue, we propose MFR, which introduces low-pass filters to extract regular patterns and texture features, and employs a channel–spatial attention enhanced autoencoder to better capture spatio-temporal characteristics of traffic data.**

📄 **Published in:** Pattern Recognition (PR), 2025  
🔗 **Paper:** [Paper Link](https://www.sciencedirect.com/science/article/abs/pii/S003132032400966X)

---

## ⚙️ Pipeline

<p align="center">
  <img src="Model.png" width="50%" />
</p

---

## 📚 Datasets
- DataCon2020 dataset is collected from https://datacon.qianxin.com/opendata. 
- CIC-IDS2017 dataset is downloaded from https://www.unb.ca/cic/datasets/ids-2017.html. 
- USTC-TFC2016 dataset is downloaded from https://github.com/echowei/DeepTraffic.


---

## 🏃‍♀️ Requirement
**Hardware** : NVIDIA GeForce RTX 3090 GPU.  
**Software** : Ubuntu 18.04 LTS + Python 3.9 + Pytorch 1.8.

---

## 📦 Code Architecture
- Our model architecture is stored in model.py, which can be easily embedded into your projects.
- The corresponding loss is stored in loss.py.

---

## 📌 Citation

If you find this work useful, please cite us:
```bibtex
@article{lian2025semi,
title = {Semi-supervised anomaly traffic detection via multi-frequency reconstruction},
author = {Xinglin Lian and Yu Zheng and Zhangxuan Dang and Chunlei Peng and Xinbo Gao},
journal = {Pattern Recognition},
pages = {111215},
year = {2025},
publisher={Elsevier}
}
```
