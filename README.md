# Country-Aware Road Damage Detection

> Experimental analysis of country-specific dataset balancing for road damage detection on the India subset of the RDD2022 benchmark.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![YOLO](https://img.shields.io/badge/YOLO-v11-green)
![Computer Vision](https://img.shields.io/badge/Task-Object%20Detection-orange)
![Research](https://img.shields.io/badge/Type-Research-purple)

---

## Abstract

Road damage detection is a fundamental computer vision problem for intelligent transportation systems, enabling automated road inspection while reducing the cost and subjectivity of manual surveys.

Although modern object detectors achieve strong performance on large multi-country datasets, regional variations in road conditions and class distributions remain largely unexplored.

This work investigates whether **country-aware dataset balancing** can improve object detection performance on the **India subset of the RDD2022 benchmark**.

Starting from the attention-enhanced YOLO framework proposed by **Wang et al.**, this project reproduces the original experimental pipeline before evaluating three targeted improvements:

- Country-aware dataset balancing
- Test-Time Augmentation (TTA)
- Architecture modification

Among the evaluated methods, dataset balancing produced the largest improvement in detection performance while maintaining a simple and reproducible training pipeline.

---

## Highlights

✅ Reproduced the IEEE BigData 2022 road damage detection framework.

✅ Designed a country-aware balancing strategy for the India subset.

✅ Improved Peak F1 score from **0.39 → 0.59**.

✅ Evaluated multiple experimental strategies under identical settings.

✅ Performed detailed dataset analysis and class imbalance visualization.
