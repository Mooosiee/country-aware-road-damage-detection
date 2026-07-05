# Country-Aware Road Damage Detection
### Experimental Analysis of Dataset Balancing for Road Damage Detection on the India Subset of RDD2022

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![YOLO](https://img.shields.io/badge/YOLO-v11-green)
![Task](https://img.shields.io/badge/Task-Object%20Detection-orange)
![Research](https://img.shields.io/badge/Type-Undergraduate%20Research-purple)

</p>

---

## Abstract

Road damage detection plays an important role in intelligent transportation systems by enabling automated inspection of road infrastructure while reducing the cost and subjectivity associated with manual surveys.

Although recent deep learning models have achieved strong performance on multi-country road damage datasets, they often treat geographically diverse datasets as a single homogeneous domain. However, road conditions, damage distributions, imaging conditions, and class frequencies vary significantly across different countries.

This work investigates whether **country-specific dataset balancing** can improve detection performance on the **India subset of the RDD2022 benchmark dataset**.

Starting from the attention-based YOLO framework proposed by Wang et al., this project reproduces the original experimental pipeline before systematically evaluating the effect of:

- Country-aware dataset balancing
- Test-Time Augmentation (TTA)
- Architecture modification

The experimental results demonstrate that reducing country-specific class imbalance provides the largest improvement in detection performance while maintaining a simple and reproducible training pipeline.

---

# Motivation

The RDD2022 dataset combines road images collected from multiple countries under different road conditions, weather patterns, camera systems and damage distributions.

During reproduction of the original paper, an important observation emerged:

> The India subset consistently demonstrated lower detection performance compared to several other countries.

This raised an important research question:

> **Can adapting the training data specifically for India improve road damage detection performance?**

Instead of proposing an entirely new detection architecture, this work focuses on improving the quality of the training data through country-aware balancing and evaluates whether this alone can produce measurable improvements.

---

# Research Contributions

This project makes the following contributions:

- Successfully reproduced the baseline implementation proposed by Wang et al.
- Performed detailed exploratory analysis of the India subset within the RDD2022 dataset.
- Identified severe country-specific class imbalance as a major limitation.
- Designed a country-aware balancing strategy using selective oversampling and augmentation.
- Evaluated multiple experimental strategies under identical training settings.
- Compared the effectiveness of balancing, Test-Time Augmentation and architectural modification using standard object detection metrics.

---

# Dataset

Experiments were conducted using the **RDD2022** benchmark dataset.

**Dataset Overview**

- Multi-national road damage benchmark
- 47,420 road images
- Six countries
- Four road damage categories
- Bounding-box annotations

For this study only the **India subset** was used.

The dataset was divided into:

| Split | Ratio |
|--------|------|
| Training | 70% |
| Validation | 20% |
| Test | 10% |

The train, validation and test sets remained fixed throughout all experiments to ensure fair comparison.

---

# Methodology

The overall experimental workflow is illustrated below.

```
RDD2022 Dataset
        │
        ▼
 India Subset Extraction
        │
        ▼
 Dataset Analysis
        │
        ▼
 Country-aware Dataset Balancing
        │
        ▼
 YOLO Baseline Training
        │
        ▼
──────────────────────────────────────
Experiment 1 : Baseline
Experiment 2 : Balanced Dataset
Experiment 3 : Test-Time Augmentation
Experiment 4 : Architecture Modification
──────────────────────────────────────
        │
        ▼
 Performance Evaluation
```

---

# Experiments

## Experiment 1 — Baseline

The baseline detector was trained on the original India subset without modifying the dataset.

Purpose:

- Establish reference performance.
- Identify failure cases.
- Analyze class-wise detection performance.

---

## Experiment 2 — Country-Aware Dataset Balancing

The severe class imbalance observed within the India subset motivated a balancing strategy.

Instead of balancing the global dataset, balancing was performed specifically on the India subset using:

- Targeted oversampling
- Data augmentation
- Controlled train-only balancing

Validation and test sets were intentionally left untouched to prevent data leakage.

---

## Experiment 3 — Test-Time Augmentation

Test-Time Augmentation (TTA) was applied during inference without retraining the model.

Predictions from multiple augmented versions of each image were merged before Non-Maximum Suppression to evaluate whether inference-time augmentation improves localization performance.

---

## Experiment 4 — Architecture Modification

An additional architectural modification was evaluated to determine whether network-level changes could further improve performance beyond dataset balancing.

The experiment was performed under the same evaluation protocol to enable direct comparison.

---

# Experimental Results

| Experiment | Peak F1 | mAP@0.5 | mAP@0.5:0.95 | Observation |
|------------|---------|----------|---------------|-------------|
| Baseline | 0.39 | 0.339 | 0.144 | Reference model |
| Balanced Dataset | **0.59** | 0.563 | 0.366 | Largest improvement |
| Balanced + TTA | 0.58 | **0.591** | **0.385** | Better localization |
| Architecture Modification | 0.57 | 0.559 | 0.353 | Limited improvement |

---

# Key Findings

The conducted experiments produced several important observations.

- Country-specific class imbalance significantly affects detector performance.
- Dataset balancing produced the largest improvement among all evaluated methods.
- Test-Time Augmentation improved localization metrics but produced only marginal changes in Peak F1.
- Architectural modification alone was insufficient to outperform dataset balancing.
- Improving data quality proved more effective than increasing model complexity for the evaluated setting.

---

# Repository Structure

```
country-aware-road-damage-detection/

├── docs/
│   ├── Dataset_Analysis.pdf
│   ├── Research_Report.pdf
│   └── Literature_Review.pdf
│
├── experiments/
│   ├── baseline.md
│   ├── balancing.md
│   ├── tta.md
│   └── architecture.md
│
├── figures/
│   ├── methodology.png
│   ├── pipeline.png
│   ├── confusion_matrix.png
│   ├── class_distribution.png
│   ├── predictions.png
│   └── results.png
│
├── notebooks/
├── scripts/
├── models/
├── requirements.txt
└── README.md
```

---

# Future Work

Several research directions remain open.

- Evaluate balancing strategies across all countries within RDD2022.
- Explore domain adaptation techniques for cross-country generalization.
- Investigate lightweight deployment-oriented object detectors.
- Incorporate attention mechanisms into the balanced training pipeline.
- Extend evaluation to newer YOLO architectures.

---

# Acknowledgements

This work was completed as part of an undergraduate research internship at **ABV-IIITM Gwalior**.

The implementation and experimental pipeline build upon the work presented in:

> Wang et al., *An Ensemble Learning Approach with Multi-depth Attention Mechanism for Road Damage Detection*, IEEE BigData 2022.

---

# Citation

If this repository is useful in your work, please consider citing the original paper.

```bibtex
@inproceedings{wang2022roaddamage,
  title={An Ensemble Learning Approach with Multi-depth Attention Mechanism for Road Damage Detection},
  author={Wang, Shouxing and others},
  booktitle={IEEE International Conference on Big Data},
  year={2022}
}
```

---

# License

This repository is released for research and educational purposes.

The original implementation and pretrained models belong to their respective authors.
